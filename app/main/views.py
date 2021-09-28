from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .. import db,photos
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required,current_user


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to PitchWorld'

    # Getting reviews by category
    interview_pitches = Pitch.get_pitches('interview')
    product_pitches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')


    return render_template('index.html',title = title, interview = interview_pitches, product = product_pitches, promotion = promotion_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches_count)


"""add a category section

Revision ID: 9ecf23693c14
Revises: 2e2d28d226ef
Create Date: 2021-09-28 09:05:15.843666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ecf23693c14'
down_revision = '2e2d28d226ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
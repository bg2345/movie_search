"""empty message

Revision ID: 25db39703081
Revises: 
Create Date: 2019-05-03 03:20:18.933124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25db39703081'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('director',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('imdb', sa.String(length=56), nullable=True),
    sa.Column('profile', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('original_title', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_title'), 'movie', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movie_title'), table_name='movie')
    op.drop_table('movie')
    op.drop_table('director')
    # ### end Alembic commands ###

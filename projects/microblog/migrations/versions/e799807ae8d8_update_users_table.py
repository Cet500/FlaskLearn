"""update users table

Revision ID: e799807ae8d8
Revises: 9cd08651c8d5
Create Date: 2021-03-16 19:35:55.657018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e799807ae8d8'
down_revision = '9cd08651c8d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_image', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('datetime_upd', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('user', sa.Column('sex', sa.String(length=1), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'sex')
    op.drop_column('user', 'description')
    op.drop_column('user', 'datetime_upd')
    op.drop_column('user', 'avatar_image')
    # ### end Alembic commands ###

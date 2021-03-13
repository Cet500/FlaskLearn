"""posts table

Revision ID: 834ab8a70342
Revises: 97bba79e4ad1
Create Date: 2021-03-13 17:57:58.924359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '834ab8a70342'
down_revision = '97bba79e4ad1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('lastname', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('pass_hash', sa.String(length=128), nullable=False),
    sa.Column('datetime_reg', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_login'), 'user', ['login'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('message', sa.String(length=200), nullable=True),
    sa.Column('datetime_add', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_login', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('login', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('lastname', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('pass_hash', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('datetime_reg', mysql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_users_login', 'users', ['login'], unique=True)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.drop_table('post')
    op.drop_index(op.f('ix_user_login'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

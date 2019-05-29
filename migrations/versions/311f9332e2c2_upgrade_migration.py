"""upgrade migration

Revision ID: 311f9332e2c2
Revises: 
Create Date: 2019-05-28 13:02:26.144005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311f9332e2c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(length=500), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('author', sa.String(length=250), nullable=True),
    sa.Column('categ', sa.String(length=250), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('pitch_title', sa.String(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('about', sa.String(length=500), nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile', sa.String(length=250), nullable=True))
    op.add_column('users', sa.Column('username', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'username')
    op.drop_column('users', 'profile')
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'about')
    op.drop_table('comments')
    op.drop_table('pitches')
    # ### end Alembic commands ###
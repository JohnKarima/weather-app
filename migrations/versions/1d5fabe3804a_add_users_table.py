"""add users table

Revision ID: 1d5fabe3804a
Revises: b7ad46a43297
Create Date: 2020-09-29 11:34:01.672170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d5fabe3804a'
down_revision = 'b7ad46a43297'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###

"""empty message

Revision ID: 496d44f4b5c0
Revises: 22cf290bfac7
Create Date: 2017-12-28 08:22:06.731540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '496d44f4b5c0'
down_revision = '22cf290bfac7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    # ### end Alembic commands ###

"""test

Revision ID: ee82191ef763
Revises: 45cebf10c69a
Create Date: 2021-10-29 15:59:31.729319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee82191ef763'
down_revision = '45cebf10c69a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('test', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'test')
    # ### end Alembic commands ###

"""empty message

Revision ID: 32f6c8170253
Revises: ee82191ef763
Create Date: 2021-10-29 16:00:22.610763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f6c8170253'
down_revision = 'ee82191ef763'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('test', sa.VARCHAR(length=10), nullable=False))
    # ### end Alembic commands ###

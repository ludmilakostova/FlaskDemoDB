"""add new column test

Revision ID: 5b6bd7d186c7
Revises: c9826da0742b
Create Date: 2023-02-18 14:38:25.024094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b6bd7d186c7'
down_revision = 'c9826da0742b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('test_something', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'test_something')
    # ### end Alembic commands ###

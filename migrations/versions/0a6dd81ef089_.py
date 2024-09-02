"""empty message

Revision ID: 0a6dd81ef089
Revises: 7c61cae5cf8d
Create Date: 2024-07-17 07:33:12.479152

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a6dd81ef089'
down_revision = '7c61cae5cf8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('new_col')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('new_col', mysql.VARCHAR(length=126), nullable=True))

    # ### end Alembic commands ###

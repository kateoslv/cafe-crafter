"""Update product description length and replace user name to first_name

Revision ID: 2758edc823ed
Revises: 9617ad06ac66
Create Date: 2025-02-01 22:26:36.269278

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '2758edc823ed'
down_revision: Union[str, None] = '9617ad06ac66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'description',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.add_column('users', sa.Column('first_name', sa.String(length=30), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', mysql.VARCHAR(length=30), nullable=False))
    op.drop_column('users', 'first_name')
    op.alter_column('products', 'description',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###

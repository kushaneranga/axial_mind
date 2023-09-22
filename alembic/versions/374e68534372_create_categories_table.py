"""create categories table

Revision ID: 374e68534372
Revises: 
Create Date: 2023-09-19 01:43:54.575890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '374e68534372'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('slug', sa.String(255), nullable=False),
        sa.Column('thumbnail', sa.Text, nullable=True),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('parent_id', sa.Integer, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=False, default=False),
        sa.Column('is_feature', sa.Boolean, nullable=False, default=False),
        sa.Column('order', sa.Integer, nullable=True),
        sa.Column('meta_title', sa.String(255), nullable=True),
        sa.Column('meta_keywords', sa.String(255), nullable=True),
        sa.Column('meta_h1', sa.String(255), nullable=True),
        sa.Column('meta_canonical', sa.String(255), nullable=True),
        sa.Column('meta_description', sa.Text, nullable=True),
        sa.Column(sa.TIMESTAMP()),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_category_id'), 'categories', ['id'], unique=True)
    op.create_index(op.f('ix_category_name'), 'categories', ['name'], unique=True)
    op.create_index(op.f('ix_category_slug'), 'categories', ['slug'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_category_id'), table_name='categories')
    op.drop_index(op.f('ix_category_name'), table_name='categories')
    op.drop_index(op.f('ix_category_slug'), table_name='categories')
    op.drop_table('categories')

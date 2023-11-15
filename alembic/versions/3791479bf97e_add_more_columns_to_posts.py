"""add_more_columns_to_posts

Revision ID: 3791479bf97e
Revises: 144d6e921121
Create Date: 2023-11-15 06:35:46.589648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3791479bf97e'
down_revision: Union[str, None] = '144d6e921121'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('description',sa.String() ,nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'description')
    pass

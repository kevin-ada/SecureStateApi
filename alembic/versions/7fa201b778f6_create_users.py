"""create_users

Revision ID: 7fa201b778f6
Revises: 3791479bf97e
Create Date: 2023-11-15 06:47:14.261500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7fa201b778f6'
down_revision: Union[str, None] = '3791479bf97e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

"""auto-populate remaining tables

Revision ID: ed807ad1b4d1
Revises: c24d7b6d69e5
Create Date: 2023-11-15 07:16:54.806984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed807ad1b4d1'
down_revision: Union[str, None] = 'c24d7b6d69e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('posts_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('address', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('city', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('state', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('zipcode', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('posts', sa.Column('price', sa.Float(), nullable=False))
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_column('posts', 'price')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'zipcode')
    op.drop_column('posts', 'state')
    op.drop_column('posts', 'city')
    op.drop_column('posts', 'address')
    op.drop_table('Votes')
    op.drop_table('Images')
    # ### end Alembic commands ###

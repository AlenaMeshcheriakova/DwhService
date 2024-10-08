"""init

Revision ID: 74868a91f5d5
Revises: d6bfcc96ec19
Create Date: 2024-08-09 19:45:12.300926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74868a91f5d5'
down_revision: Union[str, None] = 'd6bfcc96ec19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    actionEnum = sa.Enum('CREATED', 'UPDATED', 'DELETED', name='action_dwh_enum', create_type=False)
    op.create_table('group_dwh',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('group_id', sa.Uuid(), nullable=False),
    sa.Column('action', actionEnum, nullable=False),
    sa.Column('group_name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('created_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level_dwh',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('level_id', sa.Uuid(), nullable=False),
    sa.Column('action', actionEnum, nullable=False),
    sa.Column('lang_level', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('created_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('lang_level')
    )
    op.create_table('user_dwh',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('action', actionEnum, nullable=False),
    sa.Column('telegram_user_id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('training_length', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('created_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('word_dwh',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('word_id', sa.Uuid(), nullable=False),
    sa.Column('action', actionEnum, nullable=False),
    sa.Column('german_word', sa.String(), nullable=False),
    sa.Column('english_word', sa.String(), nullable=True),
    sa.Column('russian_word', sa.String(), nullable=False),
    sa.Column('lang_level_id', sa.Uuid(), nullable=False),
    sa.Column('word_type_id', sa.Uuid(), nullable=False),
    sa.Column('group_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('amount_already_know', sa.Integer(), nullable=False),
    sa.Column('amount_back_to_learning', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('created_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_dwh_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('word_dwh')
    op.drop_table('user_dwh')
    op.drop_table('level_dwh')
    op.drop_table('group_dwh')
    # ### end Alembic commands ###

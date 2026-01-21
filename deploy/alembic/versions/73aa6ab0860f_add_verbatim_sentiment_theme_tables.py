"""add verbatim sentiment theme tables

Revision ID: 73aa6ab0860f
Revises: 
Create Date: 2026-01-07 05:52:43.851935
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73aa6ab0860f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'verbatim',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.Text, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('source', sa.String, nullable=True)
    )

    op.create_table(
        'themes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True, nullable=False)
    )

    op.create_table(
        'sentiments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('label', sa.String, unique=True, nullable=False)
    )

    op.create_table(
        'verbatim_theme',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('verbatim_id', sa.Integer, sa.ForeignKey('verbatim.id')),
        sa.Column('theme_id', sa.Integer, sa.ForeignKey('themes.id'))
    )

    op.create_table(
        'verbatim_sentiment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('verbatim_id', sa.Integer, sa.ForeignKey('verbatim.id')),
        sa.Column('sentiment_id', sa.Integer, sa.ForeignKey('sentiments.id'))
    )


def downgrade() -> None:
    op.drop_table('verbatim_sentiment')
    op.drop_table('verbatim_theme')
    op.drop_table('sentiments')
    op.drop_table('themes')
    op.drop_table('verbatim')

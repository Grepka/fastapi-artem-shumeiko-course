"""rename hotels columns

Revision ID: 040ac36114ea
Revises: 422b54f3d3bf
Create Date: 2026-06-29 17:55:02.884773

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "040ac36114ea"
down_revision: Union[str, Sequence[str], None] = "422b54f3d3bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "hotels",
        "name",
        new_column_name="title",
        existing_type=sa.String(length=100),
        existing_nullable=False,
    )
    op.alter_column(
        "hotels",
        "city",
        new_column_name="location",
        existing_type=sa.String(length=255),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "hotels",
        "title",
        new_column_name="name",
        existing_type=sa.String(length=100),
        existing_nullable=False,
    )
    op.alter_column(
        "hotels",
        "location",
        new_column_name="city",
        existing_type=sa.String(length=255),
        existing_nullable=False,
    )

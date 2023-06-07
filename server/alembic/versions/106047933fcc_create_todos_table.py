"""create todos table

Revision ID: 106047933fcc
Revises: 
Create Date: 2023-06-04 14:26:29.906762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "106047933fcc"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        create table todos (
            id bigserial primary key,
            name text not null,
            completed boolean not null default false
        )
        """
    )


def downgrade():
    op.execute("drop table todos")

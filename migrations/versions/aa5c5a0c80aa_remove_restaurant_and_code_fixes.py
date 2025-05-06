"""Prepare migration for only the image table

Revision ID: aa5c5a0c80aa
Revises: d0c7b8e4b57c
Create Date: 2025-05-05 22:17:04.903002

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'aa5c5a0c80aa'
down_revision = 'd0c7b8e4b57c'
branch_labels = None
depends_on = None


def upgrade():
    # Create the image table
    op.create_table(
        'image',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uploader', sa.String(length=30), nullable=False),
        sa.Column('image_url', sa.String(length=255), nullable=False),
        sa.Column('upload_date', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    # Drop the image table
    op.drop_table('image')
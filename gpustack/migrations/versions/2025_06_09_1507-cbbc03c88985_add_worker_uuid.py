"""add_worker_uuid

Revision ID: cbbc03c88985
Revises: c45e397531d1
Create Date: 2025-06-09 15:07:05.299418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import gpustack


# revision identifiers, used by Alembic.
revision: str = 'cbbc03c88985'
down_revision: Union[str, None] = 'c45e397531d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('worker_uuid', sa.String(length=255), nullable=False, server_default=''))
    with op.batch_alter_table('model_instances') as batch_op:
        batch_op.add_column(sa.Column('ports', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('gpu_addresses', sa.JSON(), nullable=True))

    op.create_index('ix_workers_worker_uuid', 'workers', ['worker_uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workers', schema=None) as batch_op:
        batch_op.drop_column('worker_uuid')
    with op.batch_alter_table('model_instances') as batch_op:
        batch_op.drop_column('ports')
        batch_op.drop_column('gpu_addresses')

    op.drop_index('ix_workers_worker_uuid', table_name='workers')
    # ### end Alembic commands ###

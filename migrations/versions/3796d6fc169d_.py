"""empty message

Revision ID: 3796d6fc169d
Revises: eb6dad085794
Create Date: 2023-08-29 19:26:40.635886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3796d6fc169d'
down_revision = 'eb6dad085794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('starships_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('vehicles_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'vehicles', ['vehicles_id'], ['id'])
        batch_op.create_foreign_key(None, 'starships', ['starships_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehicles_id')
        batch_op.drop_column('starships_id')

    # ### end Alembic commands ###

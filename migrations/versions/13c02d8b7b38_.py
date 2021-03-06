"""empty message

Revision ID: 13c02d8b7b38
Revises: 7a5a3ab16e5f
Create Date: 2020-11-14 13:03:49.500353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c02d8b7b38'
down_revision = '7a5a3ab16e5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Betas Time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dates', sa.String(), nullable=True),
    sa.Column('beta', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('BetasTime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BetasTime',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"BetasTime_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('dates', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('beta', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='BetasTime_pkey')
    )
    op.drop_table('Betas Time')
    # ### end Alembic commands ###

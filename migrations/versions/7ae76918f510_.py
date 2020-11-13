"""empty message

Revision ID: 7ae76918f510
Revises: 77b1d0d8e8fb
Create Date: 2020-11-07 16:49:14.467513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ae76918f510'
down_revision = '77b1d0d8e8fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('BetasTime', sa.Column('beta', sa.String(), nullable=True))
    op.drop_column('BetasTime', 'alpha')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('BetasTime', sa.Column('alpha', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('BetasTime', 'beta')
    # ### end Alembic commands ###
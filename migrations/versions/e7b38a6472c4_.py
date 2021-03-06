"""empty message

Revision ID: e7b38a6472c4
Revises: 04b152ca69ac
Create Date: 2020-10-30 10:19:13.643767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7b38a6472c4'
down_revision = '04b152ca69ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('betas', sa.Column('weights', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('betas', 'weights')
    # ### end Alembic commands ###

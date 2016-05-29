"""first migration

Revision ID: 5df559291f37
Revises: None
Create Date: 2016-05-28 01:10:38.599171

"""

# revision identifiers, used by Alembic.
revision = '5df559291f37'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('date_modified', sa.DATETIME(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), nullable=False),
    sa.Column('password', sa.VARCHAR(length=192), nullable=False),
    sa.Column('role', sa.SMALLINT(), nullable=False),
    sa.Column('status', sa.SMALLINT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    ### end Alembic commands ###

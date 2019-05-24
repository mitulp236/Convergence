"""empty message

Revision ID: 5f586bd73f0c
Revises: 
Create Date: 2019-05-24 12:25:05.821414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f586bd73f0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaigner',
    sa.Column('CAMP_ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('EMAIL', sa.String(length=80), nullable=False),
    sa.Column('PASSWORD', sa.String(length=120), nullable=True),
    sa.Column('FIRSTNAME', sa.String(length=50), nullable=True),
    sa.Column('LASTNAME', sa.String(length=50), nullable=True),
    sa.Column('ENROLLMENT_NO', sa.String(length=15), nullable=True),
    sa.Column('BRANCH', sa.String(length=50), nullable=True),
    sa.Column('SEM', sa.Integer(), nullable=True),
    sa.Column('MOBILE', sa.BigInteger(), nullable=True),
    sa.Column('STATUS', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('CAMP_ID', 'EMAIL')
    )
    op.create_table('colleges',
    sa.Column('sr_no', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('college', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('sr_no')
    )
    op.create_table('events',
    sa.Column('ID', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('NAME', sa.String(length=50), nullable=True),
    sa.Column('DATE', sa.String(length=50), nullable=True),
    sa.Column('TIME', sa.String(length=50), nullable=True),
    sa.Column('VENUE', sa.String(length=80), nullable=True),
    sa.Column('DESCRIPTION', sa.String(length=5000), nullable=True),
    sa.Column('RULES', sa.String(length=5000), nullable=True),
    sa.Column('DEPARTMENT', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('log__deleted__students',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('STUDENT_KEY', sa.String(length=16), nullable=True),
    sa.Column('FIRSTNAME', sa.String(length=50), nullable=True),
    sa.Column('LASTNAME', sa.String(length=50), nullable=True),
    sa.Column('ENROLLMENT_NO', sa.String(length=15), nullable=True),
    sa.Column('BRANCH', sa.String(length=50), nullable=True),
    sa.Column('SEM', sa.Integer(), nullable=True),
    sa.Column('COLLEGE', sa.String(length=200), nullable=True),
    sa.Column('EMAIL', sa.String(length=80), nullable=True),
    sa.Column('MOBILE', sa.BigInteger(), nullable=True),
    sa.Column('REG_DATE', sa.DateTime(), nullable=False),
    sa.Column('EVENT_1', sa.String(length=80), nullable=True),
    sa.Column('EVENT_2', sa.String(length=80), nullable=True),
    sa.Column('CAMP_ID', sa.Integer(), nullable=True),
    sa.Column('DELETED_DATE', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('student_data',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('STUDENT_KEY', sa.String(length=16), nullable=False),
    sa.Column('FIRSTNAME', sa.String(length=50), nullable=True),
    sa.Column('LASTNAME', sa.String(length=50), nullable=True),
    sa.Column('ENROLLMENT_NO', sa.String(length=15), nullable=True),
    sa.Column('BRANCH', sa.String(length=50), nullable=True),
    sa.Column('SEM', sa.Integer(), nullable=True),
    sa.Column('COLLEGE', sa.String(length=200), nullable=True),
    sa.Column('EMAIL', sa.String(length=80), nullable=True),
    sa.Column('MOBILE', sa.BigInteger(), nullable=True),
    sa.Column('REG_DATE', sa.DateTime(), nullable=False),
    sa.Column('EVENT_1', sa.String(length=80), nullable=True),
    sa.Column('EVENT_2', sa.String(length=80), nullable=True),
    sa.Column('CAMP_ID', sa.Integer(), nullable=True),
    sa.Column('LAST_LOGIN', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('ID', 'STUDENT_KEY'),
    sa.UniqueConstraint('EMAIL')
    )
    op.create_table('users',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('EMAIL', sa.String(length=80), nullable=False),
    sa.Column('PASSWORD', sa.String(length=120), nullable=False),
    sa.Column('PRIVILEGE', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('EMAIL')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('student_data')
    op.drop_table('log__deleted__students')
    op.drop_table('events')
    op.drop_table('colleges')
    op.drop_table('campaigner')
    # ### end Alembic commands ###
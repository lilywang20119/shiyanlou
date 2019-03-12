"""init database

Revision ID: e35146a8d18e
Revises: 
Create Date: 2019-03-05 13:08:04.737784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e35146a8d18e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('is_disable', sa.Boolean(), nullable=True),
    sa.Column('upload_resume_url', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_table('companydetail',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=256), nullable=True),
    sa.Column('finance', sa.String(length=64), nullable=True),
    sa.Column('staff_num', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('about', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('salary', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=32), nullable=True),
    sa.Column('tags', sa.String(length=64), nullable=True),
    sa.Column('experience_requirement', sa.String(length=64), nullable=True),
    sa.Column('degree_requirement', sa.String(length=64), nullable=True),
    sa.Column('is_fulltime', sa.Boolean(), nullable=True),
    sa.Column('release_time', sa.String(length=64), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('is_disable', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('age', sa.SmallInteger(), nullable=True),
    sa.Column('work_age', sa.SmallInteger(), nullable=True),
    sa.Column('home_city', sa.String(length=64), nullable=True),
    sa.Column('job_experience', sa.Text(), nullable=True),
    sa.Column('edu_experience', sa.Text(), nullable=True),
    sa.Column('project_experience', sa.Text(), nullable=True),
    sa.Column('resume_url', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('response', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_job',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_job')
    op.drop_table('delivery')
    op.drop_table('resume')
    op.drop_table('job')
    op.drop_table('companydetail')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

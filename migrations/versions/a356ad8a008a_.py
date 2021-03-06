"""empty message

Revision ID: a356ad8a008a
Revises: 0fe73feec23d
Create Date: 2021-04-16 20:57:28.876736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a356ad8a008a'
down_revision = '0fe73feec23d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people_sw',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=50), nullable=False),
    sa.Column('skin_color', sa.String(length=50), nullable=False),
    sa.Column('eye_color', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets_sw',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.String(length=50), nullable=False),
    sa.Column('orbital_period', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.String(length=50), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.Column('gravity', sa.String(length=50), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('surface_water', sa.String(length=50), nullable=False),
    sa.Column('population', sa.String(length=50), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites_sw',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.Integer(), nullable=False),
    sa.Column('favorite_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('planets')
    op.drop_table('favorites')
    op.drop_table('people')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('height', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hair_color', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('skin_color', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('eye_color', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('birth_year', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('gender', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('homeworld', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('favorites',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('tipo', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('favorite_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('usuario_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['user.id'], name='favorites_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('planets',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('rotation_period', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('orbital_period', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('diameter', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('climate', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('gravity', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('terrain', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('surface_water', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('population', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('url', mysql.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('favorites_sw')
    op.drop_table('planets_sw')
    op.drop_table('people_sw')
    # ### end Alembic commands ###

"""fix review model serialization and constraints

Revision ID: ff5f7d14dc22
Revises: c937efe7da18
Create Date: 2025-03-26 11:48:17.929962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff5f7d14dc22'
down_revision = 'c937efe7da18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'price',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.create_index(op.f('ix_reviews_customer_id'), 'reviews', ['customer_id'], unique=False)
    op.drop_constraint('fk_reviews_item_id_items', 'reviews', type_='foreignkey')
    op.drop_constraint('fk_reviews_customer_id_customers', 'reviews', type_='foreignkey')
    op.create_foreign_key(op.f('fk_reviews_customer_id_customers'), 'reviews', 'customers', ['customer_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(op.f('fk_reviews_item_id_items'), 'reviews', 'items', ['item_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_item_id_items'), 'reviews', type_='foreignkey')
    op.drop_constraint(op.f('fk_reviews_customer_id_customers'), 'reviews', type_='foreignkey')
    op.create_foreign_key('fk_reviews_customer_id_customers', 'reviews', 'customers', ['customer_id'], ['id'])
    op.create_foreign_key('fk_reviews_item_id_items', 'reviews', 'items', ['item_id'], ['id'])
    op.drop_index(op.f('ix_reviews_customer_id'), table_name='reviews')
    op.alter_column('items', 'price',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###

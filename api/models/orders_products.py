from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base import Base

orders_products = Table(
    "orders_products",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True)
)

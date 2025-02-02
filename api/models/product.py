from models.base import Base
from typing import List
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal

class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    discount_percentage: Mapped[Decimal] = mapped_column(Numeric(3, 2))
    orders: Mapped[List["Order"]] = relationship("Order", secondary="orders_products", back_populates="products")

    def __init__(self):
        pass

    def __str__(self):
        return (
            f"Product("
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"price='{self.price})"
        )

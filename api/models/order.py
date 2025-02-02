from models.base import Base
from typing import List
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
import enum

class OrderStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    canceled = "canceled"
    returned = "returned"
    refunded = "refunded"

class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), default=OrderStatus.pending)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    customer: Mapped["User"] = relationship(back_populates="orders")
    products: Mapped[List["Product"]] = relationship("Product", secondary="orders_products", back_populates="orders")

    def __init__(self, order_date = None):
        self.order_date = order_date or datetime.now(timezone.utc)
        self.status = OrderStatus.pending

    def __str__(self):
        return (
            f"Customer: {self.customer.name}', "
            f"Order("
            f"order_date={self.order_date.strftime('%Y-%m-%d')}', "
            f"status={self.status})"
        )

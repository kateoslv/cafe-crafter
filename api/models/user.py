from models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    addresses: Mapped[List["Address"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    orders: Mapped[List["Order"]] = relationship(back_populates="customer")

    def __init__(self):
        self.addresses = []

    def __str__(self):
        address_ids = [address.id for address in self.addresses]
        return (
            f"User("
            f"name='{self.name}', "
            f"last_name='{self.last_name}', "
            f"email='{self.email}', "
            f"addresses_ids={address_ids})"
        )

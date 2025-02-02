from models.base import Base
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Address(Base):

    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street_name: Mapped[str] = mapped_column(String(50))
    number: Mapped[int] = mapped_column(Integer)
    address_line_2: Mapped[str] = mapped_column(String(50))
    neighborhood: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(30))
    state: Mapped[str] = mapped_column(String(30))
    country: Mapped[str] = mapped_column(String(20))
    postal_code: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __init__(self):
        pass

    def __str__(self):
        return (
            f"Address("
            f"street_name='{self.street_name}', "
            f"number='{self.number}', "
            f"neighborhood='{self.neighborhood}', "
            f"city='{self.city}', "
            f"state='{self.state}', "
            f"country='{self.country}', "
            f"postal_code='{self.postal_code}', "
            f"user_id='{self.user_id}')"
        )

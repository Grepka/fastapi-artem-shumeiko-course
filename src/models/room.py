from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, ForeignKey

from src.database import Base

class RoomOrm(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKet="hotel.id")
    title: Mapped[str| None]
    description: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
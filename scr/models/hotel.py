from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, String

from scr.database import Base

class HotelOrm(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(255))
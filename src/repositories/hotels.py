from src.repositories.base import BaseRepository
from src.models.hotel import HotelOrm

class HotelsRepository(BaseRepository):
    model = HotelOrm
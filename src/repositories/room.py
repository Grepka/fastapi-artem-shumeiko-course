from src.repositories.base import BaseRepository
from src.models.room import RoomOrm


class RoomRepository(BaseRepository):
    model = RoomOrm
from sqlalchemy import select, exists

from src.repositories.base import BaseRepository
from src.models.user import UserOrm
from src.schemas.user import User


class UserRepositories(BaseRepository):
    model = UserOrm
    schema = User

    async def check_exist(self, email:str) -> bool:
        stmt = select(exists().where(self.model.email == email))
        return await self.session.scalar(stmt)



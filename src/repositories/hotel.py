from sqlalchemy import select, func

from src.repositories.base import BaseRepository
from src.models.hotel import HotelOrm
from src.schemas.hotel import Hotel


class HotelRepository(BaseRepository):
    model = HotelOrm
    schema = Hotel

    async def get_all(
            self,
            title,
            location,
            per_page,
            offset
    ):
        query = select(self.model)
        if title is not None:
            query = query.filter(func.lower(self.model.title).contains(title.lower()))
        if location is not None:
            query = query.filter(func.lower(self.model.location).contains(location.lower()))
        query = query.limit(per_page).offset(offset)
        result = await self.session.execute(query)
        return [
            self.schema.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]



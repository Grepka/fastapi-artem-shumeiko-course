from typing import List
from fastapi import APIRouter, Query, Body


router = APIRouter(prefix="/hotels", tags=["Отели"])


hotels_list = [
    {"id": 1, "name": "Красная поляна", "city": "Sochi",},
    {"id": 2, "name": "Abudaby", "city": "Dubai"},
]


@router.get("/")
async def get_hotels(
        id: int | None = Query(default=None, description="ID"),
        name: str =  Query(default=None, description="Название отеля")
) -> List:
    hotels_= []
    for hotel in hotels_list:
        if id and hotel["id"] != id:
            continue
        if name and hotel["name"] != name:
            continue
        hotels_.append(hotel)
    return hotels_

@router.post("/")
async def add_hotel(
        name: str = Body(embed=True)
):
    global hotels_list
    id = hotels_list[-1]["id"] + 1
    hotels_list.append({
        "id": id,
        "name": name
    })
    return {"result": "ok"}

@router.put("/{hotel_id}")
async def reload_hotel(
        hotel_id: int,
        name: str = Body(),
        city: str = Body()
) -> dict:
    global hotels_list
    for hotel in hotels_list:
        if hotel["id"] == hotel_id:
            hotel["name"] = name
            hotel["city"] = city
            return {"result": "ok"}

    return {"result": "not ok"}

@router.patch(
    "/{hotel_id}",
        summary="Частичное обновление данных об отеле",
        description="Тут частично обновляем данные об отеле"
)
async def edit_hotel(
        hotel_id: int,
        name: str = Body(default=None),
        city: str = Body(default=None)
) -> dict:
    global hotels_list
    for hotel in hotels_list:
        if hotel["id"] == hotel_id:
            if name is not None:
                hotel["name"] = name
            if city is not None:
                hotel["city"] = city
            return {"result": "ok"}
    return {"result": "not ok"}


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id: int):
    global hotels_list
    hotels_list = [hotel for hotel in hotels_list if hotel["id"] != hotel_id]
    return {"result": "ok"}
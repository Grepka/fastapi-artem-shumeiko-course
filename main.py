from fastapi import FastAPI, Query, Body
from fastapi.openapi.docs import get_swagger_ui_html
from typing import List
import uvicorn


app = FastAPI(docs_url=None)


hotels_list = [
    {"id": 1, "name": "Красная поляна", "city": "Sochi",},
    {"id": 2, "name": "Abudaby", "city": "Dubai"},
]

@app.get("/hotels")
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


@app.post("/hotels")
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

@app.put("/hotels/{hotel_id}")
async def reload_hostel(
        hotel_id: int,
        name: str = Body(),
        city: str = Body()
) -> dict:
    global hotels_list
    for hostel in hotels_list:
        if hostel["id"] == hotel_id:
            hostel["name"] = name
            hostel["city"] = city
            return {"result": "ok"}

    return {"result": "not ok"}

@app.patch(
    "/hotels/{hotel_id}",
        summary="Частичное обновление данных об отеле",
        description="Тут частично обновляем данные об отеле"
)
async def edit_hostel(
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


@app.delete("/hotels/{hotel_id}")
async def delete_hotel(hotel_id: int):
    global hotels_list
    hotels_list = [hotel for hotel in hotels_list if hotel["id"] != hotel_id]
    return {"result": "ok"}



@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
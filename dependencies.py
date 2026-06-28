from typing import Annotated
from fastapi import Depends, Query
from pydantic import BaseModel


class PagePagination(BaseModel):
    page: Annotated[int | None, Query(default=None, ge=1, le=100)]
    per_page: Annotated[int | None, Query(default=5, ge=5, le=100)]

PaginationDepends = Annotated[PagePagination, Depends()]
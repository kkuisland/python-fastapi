from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/request_body", tags=["Request Body"])


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.post("/items", summary="Pydantic BaseModel")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@router.put("/items/{item_id}", summary="Request Body + Path Parameters")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


@router.put("/items/path/{item_id}", summary="Request Body + Path Parameters + Query Parameters")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

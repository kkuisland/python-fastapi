from typing import Annotated

from fastapi import APIRouter, Query

router = APIRouter(prefix="/validations", tags=["Validations"])


@router.get("/items", summary="Query parameter validations, Annotated")
async def read_items(q: Annotated[str | None, Query(max_length=10)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/items/old", summary="Query parameter validations, old")
async def read_items(q: str | None = Query(default=None, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

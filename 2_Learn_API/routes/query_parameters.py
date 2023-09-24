from fastapi import APIRouter

router = APIRouter(prefix="/query_parameters", tags=["Query Parameters"])

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    """ 쿠리 매개변수 """
    # skip 과 limit 은 기본값이 있으므로,
    # /items?skip=0&limit=10 과 /items 는 같은 의미를 가진다.
    # /items?skip=10&limit=20 과 같이 skip 과 limit 을 지정할 수 있다.
    # /items?skip=10 과 같이 skip 만 지정할 수도 있다.
    # /items?limit=10 과 같이 limit 만 지정할 수도 있다.
    # return fake_items_db[skip: skip + limit]


@router.get("/items/{item_id}", summary="Optional parameters")
async def read_item(item_id: str, q: str | None = None):
    # q 는 선택사항이며 None 이 기본값이다.
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@router.get("/items/bool/{item_id}", summary="Query Parameter Type conversion")
async def read_item(item_id: str, q: str = None, short: bool = False):
    # ! 1, True, true, on, yes 는 모두 True 로 변환된다.
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.get("/users/{user_id}/items/{item_id}", summary="Multiple path and query parameters")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.get("/items/required/{item_id}", summary="Required query parameters")
async def read_user_item(item_id: str, needy: str):
    # 기본값을 선언하지 않으면 필수 쿼리 매개변수로 선언
    item = {"item_id": item_id, "needy": needy}
    return item


@router.get("/items/limit/{item_id}", summary="Optional query parameters with defaults")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

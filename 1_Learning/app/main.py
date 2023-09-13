from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 라우터 전부 가져오기
from app.routers import __all__ as routers

# 스웨거 api/v1 설정
app = FastAPI(
    title="Sample API",
    version="1.0.0",
    description="Sample API 서버입니다.",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    openapi_url="/openapi.json",
)

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])
# 라우터 등록, Root Path 설정
for router in routers:
    app.include_router(router, prefix="/api/v1")

# uvicorn main:app --reload 저장시 자동 리로드
print("========== 서버 시작 ==========")


def get_full_name(first_name: str, last_name="insoo"):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def process_times(items: list[str]):
    # print(list(enumerate(items)))  # index, value 형태 변환
    for index, item in enumerate(items, start=1):  # enumerate(리스트 객체, 인덱스 시작 값 설정)
        print(index, item)


def process_item(item: int | str):  # << 3.10 , 3.6+ >> Union[int, str], from typing import Union
    print(item)


process_item("d")

process_times(["kku", "insoo", "miso"])

print(get_full_name("kku"))

print("========== API 영역 ==========")

#
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None
#
#
# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

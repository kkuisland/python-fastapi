import asyncio
import uvicorn
import uuid
from fastapi import FastAPI
from routes import __all__ as routers

app = FastAPI(description="This is a very fancy project.")

for router in routers:
    app.include_router(router)


@app.get("/")
async def health_check():
    return {
        "message": "OK"
    }


@app.get("/{name}")
async def generate_id_for_name(name: str):
    return {
        "id": str(uuid.uuid4()),
        "name": name
    }


# 설정: uvicorn main:app --reload --port 28702
async def main():
    config = uvicorn.Config('main:app', port=28702, log_level='info', reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())

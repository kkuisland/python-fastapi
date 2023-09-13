from fastapi import APIRouter, Request

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def sample_list(request: Request):
    return {"message": "user list", "root_path": request.scope.get("root_path")}

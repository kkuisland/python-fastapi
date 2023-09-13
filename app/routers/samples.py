from fastapi import APIRouter, Request

router = APIRouter(prefix="/samples", tags=["samples"])


@router.get("/")
def sample_list(request: Request):
    return {"message": "sample list", "root_path": request.scope.get("root_path")}

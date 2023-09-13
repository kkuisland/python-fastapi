# fastapi __init__ 라우터 설정
from .samples import router as samples_router
from .users import router as users_router

__all__ = [samples_router, users_router]
# Path: app/routers/samples.py
# from fastapi import APIRouter, Request

from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException

from plombery.config import settings




def setup_cors(app: FastAPI):
    origins: List[str] = []

    if settings.allowed_origins == "*":
        origins.append("*")
    else:
        origins = [str(origin) for origin in settings.allowed_origins]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

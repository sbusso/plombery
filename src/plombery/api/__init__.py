from fastapi import FastAPI
from fastapi.responses import JSONResponse

from plombery.api.authentication import build_auth_router
from plombery._version import __version__
from plombery.websocket import asgi
from plombery.api.middlewares import setup_cors
from plombery.api.routers import pipelines, runs


API_PREFIX = "/api"

app = FastAPI(title="Plombery", version=__version__, redirect_slashes=False)

# Mount the Socket.IO server at its standard path
app.mount("/socket.io", asgi)

setup_cors(app)

app.include_router(pipelines.router, prefix=API_PREFIX)
app.include_router(runs.router, prefix=API_PREFIX)
app.include_router(build_auth_router(app), prefix=API_PREFIX)

@app.get("/health")
async def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "version": __version__
        }
    )

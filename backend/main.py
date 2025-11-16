from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import os

app = FastAPI()


@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI"}


# The --chdir flag in the Procfile makes the /backend directory the current working directory.
# We need to go up one level to find the /frontend/build directory.
build_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend", "build")
)

app.mount(
    "/static", StaticFiles(directory=os.path.join(build_dir, "static")), name="static"
)


@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    return FileResponse(os.path.join(build_dir, "index.html"))

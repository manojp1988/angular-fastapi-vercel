from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Congratulations, FASTAPI is working"}


templates = Jinja2Templates(directory="./dist/browser")

# Mounts the `static` folder within the `build` folder to the `/static` route.
app.mount("/assets", StaticFiles(directory="./dist/browser"), "assets")


# Defines a route handler for `/*` essentially.
# NOTE: this needs to be the last route defined b/c it's a catch all route

@app.get("/{rest_of_path:path}")
async def ui(req: Request, rest_of_path: str):
    return templates.TemplateResponse("index.html", {"request": req})

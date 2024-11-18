from fastapi import FastAPI

from routes import init_app

app = FastAPI()

init_app(app)

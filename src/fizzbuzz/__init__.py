from fastapi import FastAPI

from src.fizzbuzz.config import settings
from src.fizzbuzz.entrypoints.router import router as api_router


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    return app


app = get_application()
app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import APIRouter, status

from src.fizzbuzz.entrypoints.schemas import FizzBuzzIn, FizzBuzzOut
from src.fizzbuzz.service_layer import services

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/compute", response_model=FizzBuzzOut, status_code=status.HTTP_200_OK)
def compute_string(params: FizzBuzzIn):
    return

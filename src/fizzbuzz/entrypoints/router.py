from fastapi import APIRouter, status, Response

from src.fizzbuzz.entrypoints.schemas import FizzBuzzIn
from src.fizzbuzz.service_layer import services
from src.fizzbuzz.service_layer.exceptions import CannotCompute

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/compute", status_code=status.HTTP_200_OK)
def compute_string(params: FizzBuzzIn, response: Response):
    try:
        computed_string = services.compute_fizzbuzz(**params.dict())
    except CannotCompute as err:
        response.status_code = 400
        return {"error": err.message}
    else:
        return {"computed_string": computed_string}

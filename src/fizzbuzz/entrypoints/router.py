from fastapi import APIRouter, status, Response

from src.fizzbuzz.cache import update_cache, InMemoryCache, most_popular_request
from src.fizzbuzz.entrypoints.schemas import FizzBuzzIn
from src.fizzbuzz.service_layer import services
from src.fizzbuzz.service_layer.exceptions import CannotCompute

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/compute", status_code=status.HTTP_200_OK)
async def compute_string(params: FizzBuzzIn, response: Response):
    """
    Endpoint that compute a string like fizzbuzz given 5 parameters :
      * 2 'multiple of' integers and their dedicated string representation
      * 1 limit that end the computation loop

    Each request is cached
    """
    try:
        computed_string = services.compute_fizzbuzz(**params.dict())
    except CannotCompute as err:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": err.message}
    else:
        await update_cache(params.dict(), InMemoryCache())
        return {"computed_string": computed_string}


@router.get("/popular-request", status_code=status.HTTP_200_OK)
async def popular_request():
    """
    Endpoint that return the oldest most popular request
    """
    most_hit = await most_popular_request(InMemoryCache())
    if not most_hit:
        return {"warning": "No request made yet"}

    return most_hit

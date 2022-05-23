from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = "FizzBuzz"
    VERSION = "1.0.0"
    API_PREFIX = "/api"


settings = Settings()

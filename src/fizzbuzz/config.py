from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = "FizzBuzz"
    VERSION = "1.0.0"
    API_PREFIX = "/api"

    FIRST_SUPERUSER = "friedrich@frederic.fred"
    FIXTURES_PATH = "/backend/app/db/fixtures"


settings = Settings()

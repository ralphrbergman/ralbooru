from fastapi.templating import Jinja2Templates
from pydantic_settings import BaseSettings, SettingsConfigDict

templates = Jinja2Templates(directory = "templates")

class Settings(BaseSettings):
    NAME: str = "Ralbooru"

    model_config = SettingsConfigDict(env_file = ".env", extra = "ignore")

settings = Settings()

templates.env.globals["settings"] = settings

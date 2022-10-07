import enum
import os
import secrets
from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator


class SettingsModeEnum(str, enum.Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class Settings(BaseSettings):
    
    param: Optional[str] = "value"

settings = Settings()

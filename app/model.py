from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID
from datetime import datetime
from enum import Enum

# -------------------
# Model Definitions
# -------------------

class BaseModelConfig(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class User(BaseModelConfig):
    user_id: UUID
    username: str
    email: EmailStr
    password_hash: str
    role: str  # Consider using Enum for roles
    created_at: datetime
    updated_at: datetime

class UserTypeEnum(str, Enum):
    normal = "normal"
    admin = "admin"

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_

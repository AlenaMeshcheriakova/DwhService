import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from src.model.action_dwh_enum import ActionDWHEnum
from datetime import datetime

#---------------------Word---------------------
class WordDwhDTO(BaseModel):
    word_id: uuid.UUID
    action: ActionDWHEnum
    german_word: str
    english_word: Optional[str] = None
    russian_word: str
    lang_level_id: uuid.UUID
    word_type_id: uuid.UUID
    group_id: uuid.UUID
    user_id: uuid.UUID
    amount_already_know: int
    amount_back_to_learning: int
    created_at: datetime
    updated_at: datetime
    description: str

class WordAddDwhDTO(WordDwhDTO):
    id: uuid.UUID

class WordAddDTO(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    german_word: str = Field(max_length=63)
    english_word: Optional[str] = Field(max_length=45)
    russian_word: Optional[str] = Field(max_length=33)
    amount_already_know: int = Field(ge=0)
    amount_back_to_learning: int = Field(ge=0)
    lang_level_id: uuid.UUID
    word_type_id: uuid.UUID
    group_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

#---------------------User---------------------
class UserDwhDTO(BaseModel):
    user_id: uuid.UUID
    action: ActionDWHEnum
    telegram_user_id: str
    email: EmailStr
    hashed_password: str
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    user_name: str
    training_length: Optional[int] = 10
    created_at: datetime
    updated_at: datetime
    description: str

class UserAddDwhDTO(UserDwhDTO):
    id: uuid.UUID

class UserCreateFullDTO(BaseModel):
    id: uuid.UUID
    user_name: str = Field(max_length=35)
    telegram_user_id: str = Field(max_length=35)
    training_length: int = Field(ge=0)
    password: Optional[str] = None
    hashed_password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
    created_at: datetime
    updated_at: datetime

#---------------------Level---------------------
class LevelDwhDTO(BaseModel):
    level_id: uuid.UUID
    action: ActionDWHEnum
    lang_level: str
    created_at: datetime
    updated_at: datetime
    description: str

class LevelAddDwhDTO(LevelDwhDTO):
    id: uuid.UUID

class LevelAddDTO(BaseModel):
    id: uuid.UUID
    lang_level: str
    created_at: datetime
    updated_at: datetime

#---------------------Group---------------------

class GroupDwhDTO(BaseModel):
    group_id: uuid.UUID
    action: ActionDWHEnum
    group_name: str
    created_at: datetime
    updated_at: datetime
    description: str
    user_id: uuid.UUID

class GroupAddDwhDTO(GroupDwhDTO):
    id: uuid.UUID

class GroupAddDTO(BaseModel):
    id: uuid.UUID
    group_name: str = Field(max_length=256)
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
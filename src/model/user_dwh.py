import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base
from src.model.action_dwh_enum import ActionDWHEnum


class UserDWH(Base):
    __tablename__ = "user_dwh"

    id: Mapped[Base.get_intpk(self=Base)]
    user_id: Mapped[uuid.UUID]
    action: Mapped[ActionDWHEnum] = mapped_column(nullable=False)
    telegram_user_id: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column( default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column( default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    user_name: Mapped[str] = mapped_column(unique=False)
    training_length: Mapped[int] = mapped_column(default=10, nullable=True)

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    # DWH timing
    created_dwh_at: Mapped[Base.get_created_at(self=Base)]
    updated_dwh_at: Mapped[Base.get_updated_at(self=Base)]

    description: Mapped[str] = mapped_column(String[256])

import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base
from src.model.action_dwh_enum import ActionDWHEnum


class LevelDWH(Base):
    __tablename__ = "level_dwh"

    id: Mapped[Base.get_intpk(self=Base)]
    level_id: Mapped[uuid.UUID]
    action: Mapped[ActionDWHEnum] = mapped_column(nullable=False)
    lang_level: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    # DWH timing
    created_dwh_at: Mapped[Base.get_created_at(self=Base)]
    updated_dwh_at: Mapped[Base.get_updated_at(self=Base)]

    description: Mapped[str] = mapped_column(String[256])

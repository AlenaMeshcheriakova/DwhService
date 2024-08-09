import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base
from src.model.action_dwh_enum import ActionDWHEnum

class WordDWH(Base):
    __tablename__ = "word_dwh"

    id: Mapped[Base.get_intpk(self=Base)]
    word_id: Mapped[uuid.UUID]
    action: Mapped[ActionDWHEnum] = mapped_column(nullable=False)

    german_word: Mapped[str] = mapped_column(String[256])
    english_word: Mapped[Optional[str]] = mapped_column(String[256], nullable=True)
    russian_word: Mapped[str] = mapped_column(String[256])

    lang_level_id: Mapped[uuid.UUID]
    word_type_id: Mapped[uuid.UUID]
    group_id: Mapped[uuid.UUID]
    user_id: Mapped[uuid.UUID]
    amount_already_know: Mapped[int]
    amount_back_to_learning: Mapped[int]

    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    # DWH timing
    created_dwh_at: Mapped[Base.get_created_at(self=Base)]
    updated_dwh_at: Mapped[Base.get_updated_at(self=Base)]

    description: Mapped[str] = mapped_column(String[256])

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
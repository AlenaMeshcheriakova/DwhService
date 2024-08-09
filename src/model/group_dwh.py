import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base
from src.model.action_dwh_enum import ActionDWHEnum

class GroupDWH(Base):
    """
    Object class Group - represent group of words, which user can create and grouped by group name
    Only one group with unique name can be created for one user
    (Can be different group with the same name for different user)
    """
    __tablename__ = "group_dwh"

    id: Mapped[Base.get_intpk(self=Base)]
    group_id: Mapped[uuid.UUID]
    action: Mapped[ActionDWHEnum] = mapped_column(nullable=False)

    group_name: Mapped[str] = mapped_column(String[256])
    created_at: Mapped[Base.get_created_at(self=Base)]
    updated_at: Mapped[Base.get_updated_at(self=Base)]
    user_id: Mapped[uuid.UUID]

    # DWH timing
    created_dwh_at: Mapped[Base.get_created_at(self=Base)]
    updated_dwh_at: Mapped[Base.get_updated_at(self=Base)]

    description: Mapped[str] = mapped_column(String[256])


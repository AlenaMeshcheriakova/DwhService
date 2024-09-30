import uuid
from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound
from src.db.database import session_factory
from src.dto.schema import GroupAddDwhDTO, GroupDwhDTO
from src.log.logger import log_decorator, logger
from src.model.group_dwh import GroupDWH


class GroupDwhOrm:

    @staticmethod
    @log_decorator(my_logger=logger)
    def create_dwh_group(new_group: GroupAddDwhDTO) -> None:
        with session_factory() as session:
            stmt = insert(GroupDWH).values(**new_group.dict())
            session.execute(stmt)
            session.commit()

    @staticmethod
    @log_decorator(my_logger=logger)
    def get_group_by_id(group_id: uuid.UUID) -> Optional[GroupDwhDTO]:
        try:
            with session_factory() as session:
                group = session.execute(
                    select(GroupDWH).filter_by(id=group_id)
                ).scalars().first()
                group_dto = GroupDwhDTO(
                    group_id=group.group_id,
                    action=group.action,
                    group_name=group.group_name,
                    created_at=group.created_at,
                    updated_at=group.updated_at,
                    description=group.description,
                    user_id=group.user_id
                )
                return group_dto
        except NoResultFound:
            return None

    @staticmethod
    @log_decorator(my_logger=logger)
    def delete_group(group_id: uuid.UUID) -> bool:
        """
        Delete object by table id, not by Group ID from original table
        :param group_id: Unique id in table GroupDWH
        :return: Bool (True if object was successfully deleted)
        """
        with session_factory() as session:
            group = session.execute(
                select(GroupDWH).filter_by(id=group_id)
            ).scalars().one_or_none()
            if group:
                session.delete(group)
                session.commit()
                return True
            return False

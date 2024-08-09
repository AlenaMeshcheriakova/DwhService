import uuid
from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound
from src.db.database import session_factory
from src.dto.schema import LevelAddDwhDTO, LevelDwhDTO
from src.log.logger import log_decorator, CustomLogger
from src.model.level_dwh import LevelDWH


class LevelDwhOrm:

    @staticmethod
    @log_decorator(my_logger=CustomLogger())
    def create_dwh_level(new_level: LevelAddDwhDTO):
        with session_factory() as session:
            stmt = insert(LevelDWH).values(**new_level.dict())
            session.execute(stmt)
            session.commit()

    @staticmethod
    @log_decorator(my_logger=CustomLogger())
    def get_level_by_id(level_id: uuid.UUID) -> Optional[LevelDwhDTO]:
        try:
            with session_factory() as session:
                level = session.execute(
                    select(LevelDWH).filter_by(id=level_id)
                ).scalar_one_or_none()
                level_dto = LevelDwhDTO(
                    level_id=level.level_id,
                    action=level.action,
                    lang_level=level.lang_level,
                    created_at=level.created_at,
                    updated_at=level.updated_at,
                    description=level.description
                )
                return level_dto
        except NoResultFound:
            return None

    @staticmethod
    @log_decorator(my_logger=CustomLogger())
    def delete_level(level_id: uuid.UUID) -> bool:
        """
        Delete object by table id, not by Level ID from original table
        :param level_id: Unique id in table Level DWH
        :return: Bool (True if object was successfully deleted)
        """
        with session_factory() as session:
            level = session.execute(
                select(LevelDWH).filter_by(id=level_id)
            ).scalar_one_or_none()
            if level:
                session.delete(level)
                session.commit()
                return True
            return False

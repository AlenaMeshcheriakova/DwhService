import uuid
from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound
from src.db.database import session_factory
from src.dto.schema import UserAddDwhDTO, UserDwhDTO
from src.log.logger import log_decorator, logger
from src.model.user_dwh import UserDWH


class UserDwhOrm:

    @staticmethod
    @log_decorator(my_logger=logger)
    def create_dwh_user(new_user: UserAddDwhDTO):
        with session_factory() as session:
            stmt = insert(UserDWH).values(**new_user.dict())
            session.execute(stmt)
            session.commit()

    @staticmethod
    @log_decorator(my_logger=logger)
    def get_user_by_id(user_id: uuid.UUID) -> Optional[UserDwhDTO]:
        try:
            with session_factory() as session:
                user = session.execute(
                    select(UserDWH).filter_by(id=user_id)
                ).scalar_one_or_none()
                user_dto = UserDwhDTO(
                    user_id=user.user_id,
                    action=user.action,
                    telegram_user_id=user.telegram_user_id,
                    email=user.email,
                    password=user.password,
                    hashed_password=user.hashed_password,
                    is_active=user.is_active,
                    is_superuser=user.is_superuser,
                    is_verified=user.is_verified,
                    user_name=user.user_name,
                    training_length=user.training_length,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                    description=user.description
                )
                return user_dto
        except NoResultFound:
            return None

    @staticmethod
    @log_decorator(my_logger=logger)
    def delete_user(user_id: uuid.UUID) -> bool:
        """
        Delete object by table id, not by User ID from original table
        :param user_id: Unique id in table UserDWH
        :return: Bool (True if object was successfully deleted)
        """
        with session_factory() as session:
            user = session.execute(
                select(UserDWH).filter_by(id=user_id)
            ).scalar_one_or_none()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False

import uuid

from src.data.user_dwh_orm import UserDwhOrm
from src.dto.dwh_message import DwhMessage
from src.dto.schema import UserAddDwhDTO
from src.log.logger import log_decorator, logger
from src.service.abstract_message_handler import AbstractMessageHandler


class UserMessageHandler(AbstractMessageHandler):

    @log_decorator(my_logger=logger)
    def decide_handler(self, message):
        if message.get("object_type") == 'User':
            return self
        return None

    def handle(self, dwh_message: DwhMessage):
        self.add_dwh_user(dwh_message)

    @log_decorator(my_logger=logger)
    def add_dwh_user(self, dwh_message: DwhMessage):
        user_dto = dwh_message.object
        new_id = uuid.uuid4()
        dwh_user_dto = UserAddDwhDTO(
            id=new_id,
            user_id=user_dto.get('id'),
            action=dwh_message.action,
            telegram_user_id=user_dto.get('telegram_user_id'),
            email=user_dto.get('email'),
            hashed_password=user_dto.get('hashed_password', ''),
            password=user_dto.get('password', ''),
            is_active=user_dto.get('is_active', False),
            is_superuser=user_dto.get('is_superuser', False),
            is_verified=user_dto.get('is_verified', False),
            user_name=user_dto.get('user_name'),
            training_length=user_dto.get('training_length', 0),
            created_at=user_dto.get('created_at'),
            updated_at=user_dto.get('updated_at'),
            description=dwh_message.description
        )
        UserDwhOrm.create_dwh_user(dwh_user_dto)
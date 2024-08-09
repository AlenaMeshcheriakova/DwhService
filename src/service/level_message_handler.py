import uuid

from src.data.level_dwh_orm import LevelDwhOrm
from src.dto.dwh_message import DwhMessage
from src.dto.schema import LevelAddDwhDTO
from src.log.logger import log_decorator, CustomLogger
from src.service.abstract_message_handler import AbstractMessageHandler


class LevelMessageHandler(AbstractMessageHandler):

    @log_decorator(my_logger=CustomLogger())
    def decide_handler(self, message):
        if message.get("object_type") == 'Level':
            return self
        return None

    def handle(self, dwh_message: DwhMessage):
        self.add_dwh_level(dwh_message)

    @log_decorator(my_logger=CustomLogger())
    def add_dwh_level(self, dwh_message: DwhMessage):
        level_dto = dwh_message.object
        new_id = uuid.uuid4()
        dwh_level_dto = LevelAddDwhDTO(
            id=new_id,
            level_id=level_dto.get('id'),
            action=dwh_message.action,
            lang_level=level_dto.get('lang_level'),
            description=dwh_message.description,
            created_at=level_dto.get('created_at'),
            updated_at=level_dto.get('updated_at')
        )
        LevelDwhOrm.create_dwh_level(dwh_level_dto)
import uuid

from src.data.group_dwh_orm import GroupDwhOrm
from src.dto.dwh_message import DwhMessage
from src.dto.schema import GroupAddDwhDTO
from src.log.logger import log_decorator, logger
from src.service.abstract_message_handler import AbstractMessageHandler


class GroupMessageHandler(AbstractMessageHandler):

    @log_decorator(my_logger=logger)
    def decide_handler(self, message):
        if message.get("object_type") == 'Group':
            return self
        return None

    def handle(self, dwh_message: DwhMessage):
        self.add_dwh_group(dwh_message)

    @log_decorator(my_logger=logger)
    def add_dwh_group(self, dwh_message: DwhMessage):
        dwh_group_dto = dwh_message.object
        new_id = uuid.uuid4()
        dwh_group_dto = GroupAddDwhDTO(
            id=new_id,
            group_id=dwh_group_dto.get('id'),
            user_id=dwh_group_dto.get('user_id'),
            action=dwh_message.action,
            group_name=dwh_group_dto.get('group_name'),
            description=dwh_message.description,
            created_at=dwh_group_dto.get('created_at'),
            updated_at=dwh_group_dto.get('updated_at')
        )
        GroupDwhOrm.create_dwh_group(dwh_group_dto)
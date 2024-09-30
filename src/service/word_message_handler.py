import json
import uuid

from typing import Any

from src.data.word_dwh_orm import WordDwhOrm
from src.dto.dwh_message import DwhMessage
from src.dto.schema import WordAddDwhDTO, WordAddDTO, WordDwhDTO
from src.log.logger import log_decorator, logger
from src.service.abstract_message_handler import AbstractMessageHandler


class WordMessageHandler(AbstractMessageHandler):

    @log_decorator(my_logger=logger)
    def decide_handler(self, message):
        if message.get("object_type") == 'Word':
            return self
        return None

    def handle(self, dwh_message: DwhMessage):
        self.add_dwh_word(dwh_message)

    @log_decorator(my_logger=logger)
    def add_dwh_word(self, dwh_message: DwhMessage):
        word_obj = dwh_message.object
        new_id = uuid.uuid4()
        dwh_word_dto = WordAddDwhDTO(
            id=new_id,
            word_id=word_obj.get('id'),
            action=dwh_message.action,
            german_word=word_obj.get('german_word'),
            english_word=word_obj.get('english_word', ''),
            russian_word=word_obj.get('russian_word'),
            lang_level_id=word_obj.get('lang_level_id'),
            word_type_id=word_obj.get('word_type_id'),
            group_id=word_obj.get('group_id'),
            user_id=word_obj.get('user_id'),
            amount_already_know=word_obj.get('amount_already_know'),
            amount_back_to_learning=word_obj.get('amount_back_to_learning'),
            created_at=word_obj.get('created_at'),
            updated_at=word_obj.get('updated_at'),
            description=dwh_message.description
        )
        WordDwhOrm.create_dwh_word(dwh_word_dto)
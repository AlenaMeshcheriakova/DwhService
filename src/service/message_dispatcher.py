from src.service.abstract_message_handler import AbstractMessageHandler
from src.service.group_message_handler import GroupMessageHandler
from src.service.level_message_handler import LevelMessageHandler
from src.service.user_message_handler import UserMessageHandler
from src.service.word_message_handler import WordMessageHandler


class MessageDispatcher(AbstractMessageHandler):
    def __init__(self):
        self.handlers = {
            'Word': WordMessageHandler(),
            'User': UserMessageHandler(),
            'Group': GroupMessageHandler(),
            'Level': LevelMessageHandler()
        }

    def decide_handler(self, message):
        return self.handlers.get(message.get("object_type"), None)

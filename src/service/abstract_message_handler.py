from abc import abstractmethod, ABC
import logger
from src.dto.dwh_message import DwhMessage


class AbstractMessageHandler(ABC):

    @abstractmethod
    def decide_handler(self, message):
        pass

    def handle(self, message):
        handler = self.decide_handler(message)
        if handler:
            dwh_message = DwhMessage.from_dict(message)
            handler.handle(dwh_message)
        else:
            logger.error("No handler found for message type:", message.type)

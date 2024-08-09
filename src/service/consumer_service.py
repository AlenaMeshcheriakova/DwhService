import pika
import json

from cfg.сonfig import settings
from src.log.logger import log_decorator, CustomLogger
from src.service.message_dispatcher import MessageDispatcher

class ConsumerService:
    """
    Service for listening MQ
    """

    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.host = settings.get_MQ_HOST
        self.connection = None
        self.channel = None

    @log_decorator(my_logger=CustomLogger())
    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    @log_decorator(my_logger=CustomLogger())
    def handle_message(self, ch, method, properties, body):
        message = json.loads(body)
        dispatcher = MessageDispatcher()
        dispatcher.handle(message)
        print(f"Received {message}")

    @log_decorator(my_logger=CustomLogger())
    def start_consuming(self):
        if not self.connection or not self.channel:
            raise RuntimeError("Connection not established. Call connect() first.")

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.handle_message, auto_ack=True)
        print(f" [*] Waiting for messages in {self.queue_name}. To exit press CTRL+C")
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print("Interrupted")
        finally:
            self.connection.close()

if __name__ == '__main__':
    queue_name = settings.get_MQ_QUEUE_NAME
    consumer_service = ConsumerService(queue_name)
    consumer_service.connect()
    consumer_service.start_consuming()

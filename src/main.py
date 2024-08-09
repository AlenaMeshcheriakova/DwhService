from cfg.сonfig import settings
from src.service.consumer_service import ConsumerService

def run():
    """Start MQ consumer"""
    queue_name = settings.get_MQ_QUEUE_NAME
    consumer_service = ConsumerService(queue_name)
    consumer_service.connect()
    consumer_service.start_consuming()

if __name__ == '__main__':
    run()
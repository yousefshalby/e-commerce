from kafka import KafkaProducer
import json
from django.conf import settings

producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_BROKER_URL,
    api_version=(2, 5),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def send_message(data):
    producer.send(settings.KAFKA_TOPIC, value=data)
    producer.flush()

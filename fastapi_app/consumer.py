from kafka import KafkaConsumer
import json
import logging

consumer = KafkaConsumer(
    "my_topic",
    bootstrap_servers="kafka:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    api_version=(2, 5),
)


async def consume():
    for message in consumer:
        data = message.value
        print(f"Consumed message: {data}")
        # Process data here

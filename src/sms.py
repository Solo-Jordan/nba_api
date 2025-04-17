import json
from settings import MONGO_URL, RMQ_URL
from pika import BlockingConnection, URLParameters
from uuid import uuid4
from pymongo import MongoClient


def forward_message(from_user: str, message: str):
    """
    Forward the message to the agent queue.
    :param from_user: The user's phone number.
    :param message: The message to forward.
    :return:
    """

    last_message_id = str(uuid4())

    PHONE_BOOK = {
        "+18435346532": "jordan",
        "+16263477450": "christine",
    }

    # Connect to the database
    client = MongoClient(MONGO_URL)
    db = client.ai_projects
    collection = db["chat_history"]

    # Update last_message_id in doc
    collection.update_one(
        {"user": PHONE_BOOK[from_user], "status": "current"},
        {"$set": {"last_message_id": last_message_id}}
    )

    parameters = URLParameters(url=RMQ_URL)
    connection = BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue="tlc")
    channel.queue_bind(exchange='ai', queue="tlc", routing_key="ai.tlc")

    message = {
        "from": from_user,
        "message": message,
        "id": last_message_id
    }

    channel.basic_publish(exchange='ai', routing_key="ai.tlc", body=json.dumps(message))

    connection.close()

    return True

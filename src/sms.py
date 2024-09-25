from pika import BlockingConnection, URLParameters


def forward_message(from_user: str, message: str):
    """
    Forward the message to the agent queue.
    :param from_user: The user's phone number.
    :param message: The message to forward.
    :return:
    """

    parameters = URLParameters(url="amqp://agents:guppyfishaiagent!!@164.92.120.177:5672")
    connection = BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue="tlc")
    channel.queue_bind(exchange='ai', queue="tlc", routing_key="ai.tlc")

    message = {
        "from": from_user,
        "message": message
    }

    channel.basic_publish(exchange='ai', routing_key="ai.tlc", body=str(message))

    connection.close()

    return True

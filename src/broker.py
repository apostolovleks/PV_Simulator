import json
import logging
import sys
from typing import Callable

import pika


class Broker:
    def __init__(self, queue: str, host: str):
        self.queue = queue
        self.channel = None
        self.host = host
        self._set_broker_channel()

    def _set_broker_channel(self) -> None:
        """Set broker channel."""
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(self.host)
            )
        except pika.exceptions.AMQPConnectionError:
            logging.error("Connection is lost. Check is the server alive.")
            sys.exit(0)
        else:
            self.channel = connection.channel()
            self.channel.queue_declare(queue=self.queue)
            self.channel.confirm_delivery()

    def send_data(self, body: json, routing_key: str) -> str:
        """Send passed data to queue.

        :param body: data for sending
        :param routing_key: name of queue
        :return: delivery confirmation

        Where ack - message acknowledgement;
            nack - message non-acknowledgement.
        """

        try:
            self.channel.basic_publish(
                exchange="",
                routing_key=routing_key,
                body=body,
                properties=pika.BasicProperties(
                    content_type="text/plain",
                    delivery_mode=pika.DeliveryMode.Transient,
                ),
                mandatory=True,
            )
            return "ack"
        except pika.exceptions.UnroutableError:
            return "nack"

    def receive_data(
        self,
        callback: Callable[
            [
                pika.adapters.blocking_connection.BlockingChannel,
                pika.spec.Basic.Deliver,
                pika.spec.BasicProperties,
                bytes,
            ],
            None,
        ],
    ) -> None:
        """Receive messages from producer.
        :param callback: function on message receiving
        """
        try:
            self.channel.basic_consume(
                queue=self.queue, on_message_callback=callback, auto_ack=True
            )
        except pika.exceptions.AMQPError as e:
            logging.error(f"Unable to send event to RabbitMQ because: {e}")
        self.channel.start_consuming()

import pytest
from src import rabbitmq

def test_get_connection():
    connection = rabbitmq.get_connection()
    assert connection is not None
    connection.close()

def test_get_channel():
    connection = rabbitmq.get_connection()
    channel = rabbitmq.get_channel(connection)
    assert channel is not None
    connection.close()

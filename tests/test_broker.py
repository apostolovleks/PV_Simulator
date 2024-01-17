from conftest import test_broker


def test_set_broker_channel():
    assert test_broker.channel.is_open


def test_send_data():
    assert test_broker.send_data(body='test_message', routing_key='test_queue') == 'ack'


def test_receive_data(callback_for_test):
    test_broker.send_data(body='test_message', routing_key='test_queue')
    test_broker.receive_data(callback=callback_for_test)

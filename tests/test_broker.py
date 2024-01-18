from conftest import test_broker, callback_for_test


def test_set_broker_channel():
    """Test Broker for a setting connection."""
    assert test_broker.channel.is_open


def test_send_data():
    """Test sending data to Broker."""

    assert (
        test_broker.send_data(body="test_message", routing_key="test_queue")
        == "ack"
    )


def test_receive_data():
    """Test receiving data from Broker."""
    test_broker.send_data(body="test_message", routing_key="test_queue")
    test_broker.receive_data(callback=callback_for_test)

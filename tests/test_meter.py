from dto import Power
from meter import Meter


def test_get_meter_value():
    meter = Meter()
    value = meter.get_meter_value()
    assert isinstance(value, Power)
    assert 0 <= value.power_value <= 9

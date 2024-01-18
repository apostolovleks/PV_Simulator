from pathlib import Path

from broker import Broker
from disk_repository import DiskRepository
from dto import ResultData, Location
from pv_simulator import Photovoltaic

# Photovoltaic
test_coordinates = Location(48.137154, 11.576124)
test_surface_tilt = 45
test_surface_azimuth = 180
test_dt = "2024-01-14 14:00:00"
test_photovoltaic = Photovoltaic(
    test_coordinates, test_surface_tilt, test_surface_azimuth, test_dt
)

# Broker
test_broker = Broker("test_queue", "localhost")


def callback_for_test(channel, method, properties, body):
    message = body.decode()
    assert message == "test_message"
    channel.close()


# DiskRepository
test_file_name = Path("./test_file.csv")
test_file_columns = [
    "test_column1",
    "test_column2",
    "test_column3",
    "test_column4",
]
test_disk_repository = DiskRepository(test_file_name, test_file_columns)
test_result_data = ResultData("3", 23.3, 2.5, 2.4)

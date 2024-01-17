import json
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Location:
    latitude: float
    longitude: float


@dataclass
class Power:
    power_value: float
    dt: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_json(self):
        return json.dumps(self.__dict__)


@dataclass
class ResultData:
    dt_str: str
    household_consumption: float | str
    pv_power: float | str
    result_consumption: float | str

    # Transform all fields to str for further saving to a file
    def __post_init__(self):
        self.dt_str = str(self.dt_str)
        self.household_consumption = str(self.household_consumption)
        self.pv_power = f'{self.pv_power:.5f}'
        self.result_consumption = str(self.result_consumption)

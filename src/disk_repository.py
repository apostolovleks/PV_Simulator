import csv
from pathlib import Path
from typing import Sequence

from dto import ResultData


class DiskRepository:

    def __init__(self, csv_path: Path, columns: Sequence[str], ):
        self.path = csv_path
        self.columns = columns

    def _write_file(self, data: ResultData) -> None:
        """Write data to csv file.

        :param data: Data for writing
        """

        with open(self.path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.columns)
            writer.writerow(
                [data.dt_str, data.household_consumption, data.pv_power, data.result_consumption])

    def _add_to_file(self, data: ResultData):
        """Add data to csv file.

        :param data: Data for adding
        """

        with open(self.path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [data.dt_str, data.household_consumption, data.pv_power, data.result_consumption])

    def save_to_csv(self, data: ResultData) -> None:
        """Save data to scv file."""

        if self.path.exists():
            self._add_to_file(data=data)
        else:
            self._write_file(data=data)

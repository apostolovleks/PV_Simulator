import json
import logging
import os
from pathlib import Path

import pika
from dotenv import load_dotenv

from broker import Broker
from disk_repository import DiskRepository
from dto import Location, ResultData
from pv_simulator import Photovoltaic

load_dotenv()
logging.getLogger("pika").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def callback(channel: pika.adapters.blocking_connection.BlockingChannel,
             method: pika.spec.Basic.Deliver,
             properties: pika.spec.BasicProperties,
             body: bytes):
    household_consumption, dt_str = json.loads(body).values()
    location = Location(float(os.environ.get('LATITUDE')), float(os.environ.get('LONGITUDE')))
    pv_power = Photovoltaic(coordinates=location,
                            surface_tilt=int(os.environ.get('SURFACE_TILT')),
                            surface_azimuth=int(os.environ.get('SURFACE_AZIMUT')),
                            dt=dt_str).get_value()
    result_consumption = pv_power - household_consumption

    path = Path('../results/consumption_report.csv')
    columns = ['dt', 'household_consumption', 'pv_power', 'result_consumption']
    data = ResultData(dt_str, household_consumption, pv_power, result_consumption)
    disk = DiskRepository(path, columns)
    disk.save_to_csv(data=data)


def main():
    broker = Broker(queue='household_consumption', host=os.environ.get('HOST'))
    logging.info('Receiver is listening.')
    broker.receive_data(callback=callback)


if __name__ == '__main__':
    main()

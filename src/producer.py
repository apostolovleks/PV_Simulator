import logging
import os
import time

from dotenv import load_dotenv

from broker import Broker
from meter import Meter

load_dotenv()
logging.getLogger("pika").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    broker = Broker(queue='household_consumption', host=os.environ.get('HOST'))
    meter = Meter()
    logging.info('Producer is started.')
    while True:
        household_value = meter.get_meter_value()
        broker.send_data(body=household_value.to_json(), routing_key='household_consumption')
        time.sleep(2)


if __name__ == '__main__':
    main()

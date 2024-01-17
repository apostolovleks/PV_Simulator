import random
from datetime import datetime

from dto import Power


class Meter:

    @staticmethod
    def get_meter_value() -> Power:
        """Get generated value of household consumption."""

        power_value = round(random.uniform(0, 9), 2)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return Power(power_value=power_value, dt=dt)

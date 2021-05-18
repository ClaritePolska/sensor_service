#!/usr/bin/env python3

import time
from enviroplus import gas
import logging
import json

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y%m%d_%H%M%S_%Z%z')

logging.info("""gas.py - Print readings from the MICS6814 Gas sensor.

Press Ctrl+C to exit!

""")

try:
    while True:
        current_time = time.localtime()
        current_clock = time.strftime("%Y%m%d_%H%M%S_%Z%z", current_time)
        readings = gas.read_all()
        with open('/opt/sensor/input/' +'GAS_' + current_clock + '.json', 'w') as outfile:
            json.dump(readings, outfile)
        logging.info(readings)
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

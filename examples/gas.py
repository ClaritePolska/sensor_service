#!/usr/bin/env python3
from os import close
import time
from datetime import datetime
from enviroplus import gas

try:
    while True:
        current_time = datetime.now()
        dataTimeZone = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f%zZ')
        current_clock = current_time.strftime("%Y%m%d_%H%M%S")
        dataTime = current_time.strftime("%Y-%m-%dT%H:%M:%S")
        readings = gas.read_all()
        with open('/opt/sensor/input/' +'GAS_' + current_clock + '.json', 'w') as outfile: 
            outfile.write("{" +"\"dateTime\" : " +"\"" + dataTimeZone + "\"" + "," + str(readings) + "}")
            outfile.close()
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

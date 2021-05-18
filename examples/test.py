from datetime import datetime
current_time = datetime.now()
dataTimeZone = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f%zZ')
current_clock = current_time.strftime("%Y%m%d_%H%M%S")
dataTime = current_time.strftime("%Y-%m-%dT%H:%M:%S")

print(dataTimeZone)
print(current_clock)
print(dataTime)

from datetime import timedelta
from datetime import datetime
from time import sleep

usr_input = 15
now = datetime.now()
delta = timedelta(seconds=usr_input)
target = now + delta
while target > now:
    sleep(1)
    now = datetime.now()
    time_left = target - now
    print(f'\r{time_left}', end='')
print('Done')

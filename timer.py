from datetime import timedelta, datetime
from time import sleep

class Timer:
    _time_format = '%H:%M:%S %d/%m/%y'
    _units = {
            'M': 1000,
            's': 1000000,
            'm': 60000000,
            'h': 3600000000,
            'd': 86400000000,
            'w': 604800000000
            }

    def __init__(self, duration:str='1m', interval:float=1, default_suffix:str='m', quiet:bool=False):
        self._interval = interval
        self._default_suffix = default_suffix
        self._quiet = quiet
        self._interval_delta = timedelta(seconds=interval)
        self._duration = self._parse_duration(duration)
        if self._duration is None:
            print('Invalid duration')
        return

    def _parse_duration(self, duration: str):
        # Returns in microseconds
        result = 0
        time = ''
        for char in duration:
            if char.isdigit():
                time += char
            elif char.isalpha() and char in(self._units):
                result += int(time) * self._units[char]
            else:
                return
        # Check if suffix is omitted
        if result == 0 and len(time) > 0:
            result += int(time) * self._units[self._default_suffix]
        return result

    def wait(self):
        if self._duration is None:
            return False
        delta = timedelta(microseconds=self._duration)
        now = datetime.now()
        target = now + delta
        # Display current time and the end time.
        if not self._quiet:
            now_format = now.strftime(self._time_format)
            target_format = target.strftime(self._time_format)
            print(f'Now is  {now_format}')
            print(f'Ends at {target_format}')
        try:
            while target > now:
                now = datetime.now()
                time_left = target - now
                if not self._quiet:
                    print(f'\r{time_left}', end='')
                if self._interval > 0 and time_left > self._interval_delta:
                    sleep(self._interval)
            if not self._quiet:
                print('\rDone', end='')
        except KeyboardInterrupt as err:
            print(f'\rTime left is {target - now}', end='')
        return True


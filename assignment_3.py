# writing a class that inherits from a dictionary
import os

class ConfigDict(dict):
    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        # remember we can't use the code line immediately below as it will keep calling the __set__item recursively and error recursion depth exceeded will be thrown.
        # self[key] = value
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, value in self.items():
                fh.write(f'{key}={value}\n')



# writing a class that inherits from a dictionary
import os

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self._key = key
        self._keys = this.keys()

    def __str__(self):
        str1 = 'key "{0}" not found. Available keys: ({1})'.format(self._key, ', '.join(self._keys))
        return str1


class ConfigDict(dict):
    def __init__(self, filename):

        file_path, _ = os.path.split(os.path.abspath(filename))
        if os.path.exists(file_path):
            self._filename = filename
        else:
            raise FileNotFoundError('File path does not exist %s' % file_path)

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

    def __getitem__(self, item):
        if not item in self.keys():
            raise ConfigKeyError(self, item)
        return dict.__getitem__(self, item)







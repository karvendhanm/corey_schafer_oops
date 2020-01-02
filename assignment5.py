# writing a class that inherits from a dictionary
import os
import pickle

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self._key = key
        self._keys = this.keys()

    def __str__(self):
        return 'key "{0}" not found. Available keys: ({1})'.format(self._key, ', '.join(self._keys))


class ConfigDict(dict):

    config_directory = 'C:/Users/John/PycharmProjects/corey_schafer_oops/configs/'

    def __init__(self, config_name):

        self._filename = ConfigDict.config_directory + config_name + '.pickle'
        if os.path.isfile(self._filename):
            with open(self._filename, 'rb') as fh:
                pkl = pickle.load(fh)
                # for key, value in pkl.items():
                #     dict.__setitem__(self, key, value)
                # since the object 'pkl' is a dictionary we can just use 'update' instead of the above 2 lines of code
                self.update(pkl)

        else:
            with open(self._filename, 'wb') as fh:
                pickle.dump({}, fh)


    def __setitem__(self, key, value):
        # remember we can't use the code line immediately below as it will keep calling the __set__item recursively and error recursion depth exceeded will be thrown.
        # self[key] = value
        dict.__setitem__(self, key, value)
        with open(self._filename, 'wb') as fh:
            pickle.dump(dict(self), fh)


    def __getitem__(self, item):
        if not item in self:
            raise ConfigKeyError(self, item)
        return dict.__getitem__(self, item)







# Storing instance of an object in a pickle
# This is definitely not working.

import pickle
import os

os.chdir('./data')

class MyClass(object):
    def __init__(self, init_val):
        self.val = init_val

    def increment(self):
        self.val += 1


cc = MyClass(5)
cc.increment()
cc.increment()

# Not working
with open('datafile_2.txt', 'wb') as fh:
    pickle.dump(cc, fh, pickle.DEFAULT_PROTOCOL)

# Not working
with open('datafile_2.txt', 'rb') as fh:
    unpickled_cc=pickle.load(fh)

# Not working
print(unpickled_cc)
print(unpickled_cc.val)

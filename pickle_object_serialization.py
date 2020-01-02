# Object serialization or object persistence using pickle

import pickle
import os

## -----------
#### Execute once very important
# os.chdir('./data')
## -----------

mylist = ['a', 'b', 'c', 'd']

# writing an python object as a pickle
with open('datafile.txt', 'wb') as fh:
    pickle.dump(mylist, fh)

with open('datafile.txt', 'rb') as fh:
    unpickled_list=pickle.load(fh)

print(unpickled_list)
print(type(unpickled_list))

# Another method of object serialization using pickle
import pickle

x = pickle.dumps(['a', 'b', 1.2, False])
var = pickle.loads(x)







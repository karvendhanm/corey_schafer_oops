# in pdb, 'c' for continue, 'n' for next line, 's' for stepping into the function 'l' for list and 'h' for help and 'quit' to exit.

import pdb

values = range(1, 11)

mysum = 0
for val in values:
    mysum += val
    pdb.set_trace()

print(mysum)
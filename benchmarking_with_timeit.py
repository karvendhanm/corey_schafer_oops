# to see the execution time of various methods. From hereon this should inform me on what method i should use

import timeit

print('by index:     ', timeit.timeit(stmt="mydict['c']",setup="mydict={'a':1,'b':2, 'c':3}",  number=1000000))
print('by get:     ', timeit.timeit(stmt="mydict.get('c')",setup="mydict={'a':1,'b':2, 'c':3}",  number=1000000))





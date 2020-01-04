# benchmarking a function
import timeit

def testme(this_dict, key):
    return this_dict[key]


# print(timeit.timeit(stmt="testme(mydict, key)", setup="from __main__ import testme; mydict={'a':1,'b':2, 'c':3}; key='c'", number=1000000))
print(timeit.timeit(stmt="testme(mydict, key)", setup="from benchmarking_with_timeit import testme; mydict={'a':1,'b':2, 'c':3}; key='c'", number=1000000))
print(timeit.timeit(stmt="testme(mydict, key)", setup="testme = lambda x, y: x[y]; mydict={'a':1,'b':2, 'c':3}; key='c'", number=1000000))
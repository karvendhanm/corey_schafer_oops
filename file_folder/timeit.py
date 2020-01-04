# measuring the execution time of python code snippets.

# uncomment STARTS
# import timeit
#
# print('by index', timeit.timeit(stmt='dict_1["a"]', setup="dict_1 = {'a':1,'b':2,'c':3}", number=1000000))
# print('by get', timeit.timeit(stmt='dict_1.get("a")', setup="dict_1 = {'a':1,'b':2,'c':3}", number=1000000))
#
# mysetup = 'from math import sqrt'
# mystmt = '''
# def sqrt_ex():
#     mylist=[]
#     for x in range(100):
#         mylist.append(sqrt(x))
# '''
#
# print(timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000))
# uncomment ENDS

import timeit

mysetup = '''
dict_1 = {'a':1,'b':2,'c':3}; 
key='c';
def testme(this_dict, key):
    return this_dict[key]
'''

mystmt = "testme(dict_1, key)"

timeit.timeit(stmt=mystmt, setup=mysetup, number=1000000)





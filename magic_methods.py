# Core syntax features translate to "magic" method calls
'''
Magic method on strings
********************
var = 'hello'
var2 = ' world'

var+var2 # python reads this syntax as a method call on the L value or left value
var.__add__(var2)
*********************

Magic method on integers
************************
var3 = 5
var4 = 10

var3.__add__(var4)
*************************

Magic method on lists
**************************
var5 = ['a', 'b']
var6 = ['c', 'd']

var5.__add__(var6)
***************************
'''


# 1) 'abc' in var         var.__contains__('abc')
# 2) var == 'abc'         var.__eq__('abc')
# 3) var[1]               var.__getitem__(1)
# 4) var[1:3]             var.__getslice__(1, 3)
# 5) len(var)             var.__len__()
# 6) print(var)           var.__repr__()


class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):
        new_list =  [x+y for (x,y) in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)

aa = SumList([1, 2, 3, 4])
bb = SumList([16, 17, 18, 19])

cc = aa+bb
print(cc)





































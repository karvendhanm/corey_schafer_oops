class A(object):
    def dothis(self):
        print('This method is from class A')

class B(A):
    pass

class C(A):
    def dothis(self):
        print('This method is from class C')

class D(B, C):
    pass

d_inst = D()
d_inst.dothis()

# looking for method resolution order
D.mro()

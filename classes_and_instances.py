# object oriented programming

class simple_arithmetic():

    def __init__(self, value1 = None, value2 = None):
        self.lst = []

        if (value1 is not None) & (value2 is not None):
            self.val1 = value1
            self.val2 = value2

    def add(self):
        if (self.val1 is not None) & (self.val2 is not None) & (len(self.val1) == len(self.val2)):
            return [u_i + v_i for u_i, v_i in zip(self.val1, self.val2)]

    def sub(self):
        if (self.val1 is not None) & (self.val2 is not None) & (len(self.val1) == len(self.val2)):
            return [u_i - v_i for u_i, v_i in zip(self.val1, self.val2)]

    def div(self):


    def mul(self):


arith = simple_arithmetic()
arith.add()
arith.div()
arith.mul()
arith.sub()
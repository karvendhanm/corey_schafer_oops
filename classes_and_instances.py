# object oriented programming

class simple_arithmetic():

    def __init__(self, value1 = None, value2 = None):
        self.val1 = value1
        self.val2 = value2

    def add(self):
        if (self.val1 is not None) & (self.val2 is not None):
            if(len(self.val1) == len(self.val2)):
                return [round(u_i + v_i,3) for u_i, v_i in zip(self.val1, self.val2)]
        return None

    def sub(self):
        if (self.val1 is not None) & (self.val2 is not None):
            if(len(self.val1) == len(self.val2)):
                return [round(u_i - v_i,3) for u_i, v_i in zip(self.val1, self.val2)]
        return None

    def div(self):
        if (self.val1 is not None) & (self.val2 is not None):
            if(len(self.val1) == len(self.val2)):
                return [round(u_i/v_i,3) for u_i, v_i in zip(self.val1, self.val2)]
        return None

    def mul(self):
        if (self.val1 is not None) & (self.val2 is not None):
            if(len(self.val1) == len(self.val2)):
                return [round(u_i * v_i,3) for u_i, v_i in zip(self.val1, self.val2)]
        return None

    # def __repr__(self):
    #     print("the elements are: {} {}".format(self.val1, self.val2))


arith = simple_arithmetic([2,3,4], [4,5, 6])
print(arith)
print(arith.add())
print(arith.div())
print(arith.mul())
print(arith.sub())
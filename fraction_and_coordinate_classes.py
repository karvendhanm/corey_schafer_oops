import numpy as np

# class to handle fractions
# all the methods are magic/dunder methods
class Fraction(object):

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)

    def __repr__(self):
        return 'Fraction({},{})'.format(self.num, self.denom)

    def __add__(self, other):
        top = (self.num * other.denom) + (self.denom * other.num)
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __sub__(self, other):
        top = (self.num * other.denom) - (self.denom * other.num)
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __mul__(self, other):
        top = (self.num * other.num)
        bottom = (self.denom * other.denom)
        return Fraction(top, bottom)

    def __float__(self):
        return self.num/self.denom

    def __eq__(self, other):
        return self.__float__() == other.__float__()

    def __lt__(self, other):
        return self.__float__() < other.__float__()


frac_1 = Fraction(3, 10)
frac_2 = Fraction(4, 10)
frac_1 == frac_2
frac_1 < frac_2
frac_1 + frac_2
print(frac_1 - frac_2)
Fraction.__float__(frac_1)
print(repr(frac_1))
print(Fraction.__repr__(frac_1))
print(frac_1.__repr__())


# class to handle coordinates
class coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_list(obj):
        return list((obj.x, obj.y))

    def distance(self, other):
        '''
        the other has to be an instance/object of the class coordinate.
        '''
        if isinstance(other, coordinate):
            zip_var = zip(self.get_list(other), self.get_list(self))
            return np.sqrt(sum([(u_i - v_i)**2 for u_i, v_i in zip_var]))

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


c = coordinate(3, 4)
print(c)
print(type(c))
print(coordinate)
origin = coordinate(0, 0)
d = coordinate(7,8)
print(c.x, origin.x)
c.distance(d)



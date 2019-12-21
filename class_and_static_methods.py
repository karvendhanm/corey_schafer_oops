# class methods - for working with the class and the class data.
# static methods - for working independently of either the class or the instance.

# Example of a class method.
class InstanceCounter(object):
    count = 0

    def __init__(self, val): # these are all called instance methods because their first argument is self which denotes the instance.
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval): # instance methods are also called as bound methods as the instance is bound to the method.
        self.val = newval

    def get_val(self):
        return self.val

    # since we don't use the instance at all inside the method, it would probably
    # be more logically to make it as a class method
    # def get_count(self):
    #     return InstanceCounter.count

    @classmethod
    def get_count(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print('val of obj: %s'%(obj.get_val()))
    print('count %s'%(obj.get_count()))

print(InstanceCounter.get_count())


# Example of a static method
class InstanceCounter(object):
    count = 0
    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('hello')

print(a.val)
print(b.val)
print(c.val)

























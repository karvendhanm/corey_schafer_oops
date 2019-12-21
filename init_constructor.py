class MyNum(object):
    def __init__(self, value):
        try:
            val = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1


dd = MyNum(6.8)
dd.increment()
dd.increment()
print(dd.val)

dd = MyNum('Hello')
dd.increment()

# Class Attributes vs. Instance Attributes

class YourClass(object):
    classy = 10  # class variable

    def set_val(self):
        self.insty = 100
        # self.classy = 10000

dd = YourClass()

dd.set_val()
print(dd.classy)
print(dd.insty)

# Class Attributes vs. Instance Attributes

class YourClass(object):
    classy = 'class value'

dd = YourClass()

print(dd.classy)

dd.classy = 'inst value!'

print(dd.classy)

del dd.classy

print(dd.classy)





















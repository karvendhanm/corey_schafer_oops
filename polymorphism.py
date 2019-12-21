class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):
    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))

for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()

# Polymorphism in python hiding in plain sight
str1 = 'Amazon'
len(str1)
str1.__len__() # len(str1) is the same as str1.__len__(). One of those magic/dunder methods.
dir(str1)

dict1 = {'Microsoft':'Satya Nadella', 'Google':'Sundar Pichai'}
len(dict1)
dict1.__len__() # len(dict1) is the same as dict1.__len__(). One of those magic/dunder methods.

# Inheritance is the ability of one class inherit the attributes of another class.

class Date(object):
    def get_date(self):
        return '2019-12-20'

class Time(Date):

    def get_time(self):
        return '05:23:00'

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())


# Inheritance Examples
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s'%(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!'%(self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string!'%(self.name))


r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
f.eat('cat food')
r.swatstring()
# Enhanced Example

import random


class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        # super(Dog, self).__init__(name)  # In this method also we can call the parent class constructor instead of calling it in the method of the line directly above
        self.breed = random.choice(['Shin Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))

d = Dog('dogname')

print(d.name)
print(d.breed)
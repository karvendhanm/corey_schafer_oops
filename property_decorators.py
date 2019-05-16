# Property decorators - Getters, Setters, and Deleters
# Property decorator allows us to define a method but access it like an attribute.

class Employee():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + "." + last +"@company.com"

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("deleting fullname -->")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Doe")

# case 4: I want to delete the full name.
# sol: use property deleter

del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)


# case 3: want to set fullname like this: emp_1.fullname = 'Corey Shafer'
# sol: use property setter
emp_1.fullname = 'Corey Shafer'
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)


# case 2: want to access fullname method like an attribute and not like a method.
# sol: use the property decorator
emp_1.fullname


# solution for case 1 email problem.
# use property decorator
# Property decorator allows us to define a method but access it like an attribute.
# case 1:
# change the first name and fetch the following details
emp_1.first = "Corey"
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)
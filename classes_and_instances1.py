# Classes and Instances
class Employee():

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # either it is self.raise_amount or Employee.raise_amount


emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("Test", "User", 90000)

# calling a method of class with its object(instance).
emp_1.fullname()
# calling a method using the class itself. Since the class wouldn't know the details
# which instance to be fetched, instance has to be sent as an argument.
Employee.fullname(emp_1)

print(emp_1)  # output:  <Employee object at 0x000001E511BAE6D8>
print(Employee) # output: <class 'Employee'>

# difference between class variables and instance variables
# Class Variables (should be clear about class variable and instance variable)
# the variables that have the same value for all class instances.
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# class object.__dict__ has everything the class has stored.
print(emp_1.__dict__)
print(emp_2.__dict__)
# class.__dict__ will show even the class variables
print(Employee.__dict__)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06 # here an instance variable raise_amount is created.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)

# Regular methods, class methods and static methods
class Employee():

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    # regular methods by default takes an instance of a class as a first argument.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # either it is self.raise_amount or Employee.raise_amount

    # to make a method to take class as a first argument, use a decorator @classmethod
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("Test", "User", 90000)

import datetime
my_date = datetime.date(2019,5,16)
Employee.is_workday(my_date)

# Inheritance and subclasses




emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

Employee.set_raise_amount(1.05)

# unfortunately we can use an instance of the class to call the class method(set_raise_amount)
# and it will also work the same way.

emp_1.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)









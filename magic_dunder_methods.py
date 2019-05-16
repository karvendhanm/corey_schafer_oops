# Special (Magic/Dunder) Methods:
class Employee():
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    # regular methods by default takes an instance of a class as a first argument.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # either it is self.raise_amount or Employee.raise_amount

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    #__str__ = fullname

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("Test", "User", 90000)
len(emp_1)

print(emp_1 + emp_2)
print(emp_1)

print(len('test'))
print(str.__len__('test'))
print('tets'.__len__())

print(emp_1)  # output: Corey Schafer - Corey.Schafer@company.com
repr(emp_1)  # output: "Employee('Corey','Schafer',75000)"
str(emp_1)  # output: 'Corey Schafer - Corey.Schafer@company.com'

print(emp_1.__repr__())  # output: Employee('Corey','Schafer',75000)
print(emp_1.__str__())  # output: Corey Schafer - Corey.Schafer@company.com

# How int and str __add__() works
print(1 + 2)
print("Karvendhan" + " " + "Mani")

print(int.__add__(2,3))
print(str.__add__("Karvendhan"," Mani"))
print(int.__add__(2,3))



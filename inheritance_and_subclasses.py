# Inheritance and sub classes

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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Another method to achieve the same thing as above
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []

    def add_employee(self, employee):
        if (employee not in self.employees):
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_reportees(self):
         for emp in self.employees:
             print("-->", emp.fullname())


emp_1 = Employee("Corey", "Schafer", 75000)
emp_2 = Employee("Test", "User", 90000)
dev_1 = Developer("Karvendhan", "Mani", 80000, 'Pyhton')
dev_2 = Developer("John", "Doe", 100000, 'JavaScript')
dev_3 = Developer("Kvothe", "Bloodless", 72000, 'Sympathy')

mgr_1 = Manager("Jane", "Doe", 150000, [emp_1, emp_2, dev_1, dev_2])
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

lst = ["John Doe", "Jane Doe", "Steven Smith"]
lst.remove("Steven Smith")
print(lst)

dev_1 = Developer("Corey", "Schafer", 75000, 'Python')
dev_2 = Developer("Test", "User", 90000, 'JavaScript')

print(dev_1.email)
print(dev_1.prog_lang)

dev_1.pay
dev_1.apply_raise()
dev_1.pay

print(help(Developer))
print(Developer.__dict__)

print(dev_1.email)
print(dev_2.email)

dev_1 = Developer("Corey", "Schafer", 75000)
dev_2 = Developer("Test", "User", 90000)

print(dev_1.email)
print(dev_2.email)






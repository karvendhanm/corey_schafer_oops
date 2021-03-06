import abc

class GetSetParent(abc.ABC):
    #__metaclass__ = abc.ABCMeta  # In Python 3.x this line doesn't seem to be mandatory.

    def __init__(self, value):
        self.val = value

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod # Even if only one of the methods in a class is abstract, still the class can't be instantiated but can only be inherited.
    def showdoc(self):
        """ Write a line about the Instance """
        # abstract method does nothing. It simply has a return statement.
        return

class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super().set_val(value) # Another way of writing the same line is super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print('GetSetInt object ({0}) only accepts integer values'.format(id(self)))

class GetSetList(GetSetParent):

    def __init__(self, value = 0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print('GetSetList object len {0} stores history of values sets'.format(len(self.vallist)))


x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()









# Creating an abstract class.
# Abstract classes are not meant to instantiated. They are just meant to be subclassed
# These abstract classes ensures that all its children implement methods prescribed in the abstract class.

import abc

class GetterSetter(abc.ABC):
    __metaclass__ = abc.ABCMeta # this line seems to be optional. With or without this line it makes no difference whatsoever.

    @abc.abstractmethod
    def set_val(self, input):
        """ Set a value in the instance """
        return

    @abc.abstractmethod
    def get_val(self):
        """ Get and return a value from the instance"""
        return


class Myclass(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

x = Myclass()
print(x)

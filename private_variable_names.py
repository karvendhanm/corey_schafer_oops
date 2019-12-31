# variable name preceded by an underscore (_variable_name) is meant to be used internally
# meaning inside the class.
# variables with double underscore is not even inherited when subclassed.

class GetSet(object):
    instance_count = 0

    __mangled_name = 'no privacy!' ## variables with double underscores never gets inherited when subclassed.

    def __init__(self, value):
        self._attrval = value # preceding a variable with a single underscore designates the variable to be for internal use only.
        GetSet.instance_count += 1

    @property
    def var(self):
        print('getting the "var" attribute')
        return self._attrval

    @var.setter
    def var(self, value):
        print('setting the "var" attribute')
        self._attrval = value

    @var.deleter
    def var(self):
        print('setting the "var" attribute')
        self._attrval = None

cc = GetSet(5)
cc.var = 10
print(cc._attrval)
print(cc.__mangled_name) # this doesn't work
print(cc._GetSet__mangled_name)


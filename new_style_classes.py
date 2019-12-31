
# old style "Classic" class
class OldClass():
    pass

# new style class
class NewClass(object):
    pass

oc = OldClass()

nc = NewClass()

print(type(oc))
print(type(nc))

print(oc.__class__)
print(nc.__class__)
print(oc.__class__.__name__)
print(nc.__class__.__name__)
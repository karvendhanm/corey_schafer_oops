# YAML: "YAML AIN'T MARKUP LANGUAGE"

import yaml
import os
import json

# execute one time
# os.chdir('./data')


mydict = {'a':1, 'b':2, 'c':3}
mylist = [1, 2, 3, 4, 5]
mytuple = ('x', 'y', 'z')

# dictionary is converted to string
loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)
print(type(loaded_yaml))

# converting the string back to dictionry
dict_1 = yaml.load(loaded_yaml)
print(dict_1)
print(type(dict_1))


loaded_yaml = yaml.dump(mydict, default_flow_style=True)
print(type(loaded_yaml))
print(loaded_yaml)

print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))

print(type(literal_eval("{'a':1, 'b':2}")))
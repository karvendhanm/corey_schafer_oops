import yaml
import os

# just execute this once
# os.chdir('./data')

class MyClass(object):
    def __init__(self, init_val):
        self.val = init_val

    def increment(self):
        self.val += 1


cc = MyClass(5)
cc.increment()
cc.increment()

with open('obj.yaml', 'w') as fh:
    yaml.dump(cc, fh)

# Unlike pickles, only this part of the code is not working
with open('obj.yaml') as fh:
    inst = yaml.load(fh)
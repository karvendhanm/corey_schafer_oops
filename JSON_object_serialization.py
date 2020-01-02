import json
# remember JSON objects must have double quotes
import os

# execute it once
# os.chdir('./data')


with open('backup_config.json') as fh:
    conf = json.load(fh)

# print(conf)
# print(type(conf))

conf['newkey'] = 5.0005

with open('backup_config.json', 'w') as fh:
    json.dump(conf, fh)


# dumps and loads simply means dump to a string and load from a string respectively.
x = json.dumps({'a':[1, 2, 3], 'c':[7, 8, 9], 'b':[4, 5, 6]}) # this object is a string
print(type(x)) # as can be seen object x is of the type string
print(x)

mystruct = json.loads(x)
print(mystruct)
print(type(mystruct))

for key in mystruct:
    print(key)
    for el in mystruct[key]:
        print(f'     {el}')

import json

with open('backup_config.json') as fh:
    conf = json.load(fh)

conf


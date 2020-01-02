import yaml
import json

with open('app.yaml') as fh:
    struct = yaml.load(fh)

print(struct)
print(type(struct))

# help(json.dumps)

# let us dump struct to a string as struct as a dict isn't all that convenient to read.
str1 = json.dumps(struct, indent=4, separators=(',', ':'))
print(str1)

with open('app1.html', 'w') as fh:
    yaml.dump(str1, fh)




import json
import os

# Execute it once
# os.chdir('./data')

with open('backup_config.json') as fh:
    conf = json.load(fh)

print(conf)
print(type(conf))

# Now let us dump the conf object to the same json file 'backup_config.json' but with a new line for every key_value pair or in other words pretty printing.
with open('backup_config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',', ':'))





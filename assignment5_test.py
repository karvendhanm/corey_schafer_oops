from assignment5 import ConfigDict
import os
import pickle

# execute it one time
# os.chdir('./configs')
# os.getcwd()

cc = ConfigDict('log')

cc['son_1'] = 'Aadhuran'
cc['son_2'] = 'Aadhavan'

# The below code could be useful for creating initial dictionary
# dict_1 = {
#     'name':'karvendhan',
#     'age':34,
#     'company':'Amazon'
# }
#
#
# with open('log.pickle', 'wb') as fh:
#     pickle.dump(dict_1, fh)
#
# with open('log.pickle', 'rb') as fh:
#     dict_1 = pickle.load(fh)
#
# print(dict_1)
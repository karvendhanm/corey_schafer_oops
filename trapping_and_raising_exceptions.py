import sys
my_dict = {'a':1, "b":2, "c":3, "d":4}

key = input('please input a key: ')

try:
    print('testing for error')
    print(f'the value for {key} is {my_dict[key]}')

except KeyError:
    print('trapped error')
    print('the key '+key+' does not exist')
    #sys.exit()

print('the program continues')

# trapping two exceptions simultaneously
import sys

try:
    arg = sys.argv[1]
    num = int(arg)

except(IndexError, ValueError):
    exit('please enter an integer on the command line')

print('thanks for the int')



# with context performs automatic cleaning routines. It is also known as context manager.

file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/data/'

with open(file_path+'log.txt') as fh: # default mode is r. read mode
    for line in fh:
        print(line.rstrip())


fh = open(file_path+'log.txt')
for line in fh:
    line = line.rstrip()
    print(line)
fh.close()

# simple example of with context

class MyClass(object):
    def __enter__(self):
        print('we have entered "with"')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('error type: {}'.format(exc_type))
        print('error value: {}'.format(exc_val))
        print('error traceback: {}'.format(exc_tb))


    def sayhi(self):
        print('hi instance %s'%(id(self)))

with MyClass() as cc: # only with the "with" context the special magic methods __enter__ and __exit__ are called.
    cc.sayhi()
    5/0

print('after the "with" block')


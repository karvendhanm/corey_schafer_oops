class MyError(Exception):
    def __init__(self, *args):
        print('calling init')
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return "here's a MyError exception with a message: {0}".format(self.message)
        else:
            return "here's a MyError exception"

raise MyError

raise MyError('Houstan we have a problem')



import re

def process_date(this_date):

    if not re.search(r'^\d\d\d\d-\d\d-\d\d$', this_date):
        raise ValueError('please submit date in YYYY-MM-DD format')

    print(f'the submitted date is {this_date}')

process_date('1980-01-03')
process_date('1/3/1980')


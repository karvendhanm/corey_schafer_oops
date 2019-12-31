class MyClass(object):

    @staticmethod
    def make_error():
        print('entering make_error()')

        try:
            5/0
        except ZeroDivisionError:
            print('A number should not be divided by 0')

        print('                     exiting make_error()')

    def do_something(self):
        print('entering do_something()')
        self.make_error()
        print('                     exiting do_something()')


def some_util_func():
    print('entering some_util_func()')
    cc = MyClass()
    cc.do_something()
    print('                     exiting some_util_func()')

def some_major_func():
    print('entering some_major_func()')
    some_util_func()
    print('                     exiting some_major_func()')

def main():
    print('entering main()')
    some_major_func()
    print('                     exiting main()')

main()

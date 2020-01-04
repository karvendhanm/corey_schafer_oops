
def double(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    return 2*x

def doublelines(filename):
    with open(filename) as fh:
        newlist = [str(double(int(val))) for val in fh]
    with open(filename, 'w') as fh:
        fh.write('\n'.join(newlist))

def main():
    return double("Hello")


if __name__ == '__main__':
    print(main())
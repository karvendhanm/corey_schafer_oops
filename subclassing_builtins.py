class MyDict(dict):
    def __setitem__(self, key, value):
        print('setting a key and value')
        # super().__setitem__(key, value)
        dict.__setitem__(self, key, value)

dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print(f'{key}={dd[key]}')

# building a list whose index starts with 1

class MyList(list):

    def __getitem__(self, item):
        if item==0: raise IndexError
        if item > 0: item-=1
        return list.__getitem__(self, item)

    def __setitem__(self, key, value):
        if key==0: raise IndexError
        if key > 0: key-=1
        list.__setitem__(self, key, value)

x = MyList(['a', 'b', 'c'])
print(x)
x.append('spam')
print(x[1])
print(x[4])



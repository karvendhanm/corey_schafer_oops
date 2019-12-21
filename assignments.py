class MaxSizeList(object):
    def __init__(self, val):
        self.val = val
        self.lst = []

    def push(self, element):
        if len(self.lst) < self.val:
            self.lst.append(element)
        else:
            self.lst.pop(0)
            self.lst.append(element)

    def get_list(self):
        return self.lst













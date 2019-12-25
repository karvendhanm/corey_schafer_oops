# Class composition

import io
file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/'

class WriteMyStuff(object):
    def __init__(self, writer):
        self.writer = writer

    def write(self):
        msg = 'this is just a silly message'
        self.writer.write(msg)

write_object_1 = open(file_path+'sample.txt', 'w')
w1 = WriteMyStuff(write_object_1)
w1.write()
write_object_1.close()

write_object_2 = io.StringIO()
w2 = WriteMyStuff(write_object_2)
w2.write()

print('file object: ', open(file_path+'sample.txt', 'r').read())
print('stringIO object: ', write_object_2.getvalue())





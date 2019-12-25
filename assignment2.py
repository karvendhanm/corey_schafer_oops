import csv
import datetime
import abc
file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/data/'

class WriteFile(abc.ABC):
    def __init__(self, file_name, delimiter=','):
        self.file_name = file_path+file_name
        self.delimiter = delimiter

    @abc.abstractmethod
    def write(self, input):
        return


class LogFile(WriteFile):

    def write(self, msg):
        msg = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' '+ msg+'\n'
        with open(self.file_name, 'a+') as myfile:
            myfile.write(msg)


class DelimFile(WriteFile):

    def write(self, row):
        with open(self.file_name, 'a+') as myfile:
            writer = csv.writer(myfile, delimiter = self.delimiter)
            writer.writerow(row)








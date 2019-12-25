from datetime import datetime
import abc
file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/data/'

class WriteFile(abc.ABC):
    def __init__(self, file_name):
        self.file_name = file_path+file_name

    @abc.abstractmethod
    def write(self, input):
        return

    def write_lines(self, input):
        fh = open(self.file_name, 'a+')
        fh.write(input + '\n')
        fh.close()


class LogFile(WriteFile):

    def write(self, input):
        dt = datetime.now()
        dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
        input = f'{dt_str} {input}'
        super().write_lines(input)


class DelimFile(WriteFile):

    def __init__(self, file_name, delimiter):
        self.delimiter = delimiter
        super().__init__(file_name)

    def write(self, input):
        input = self.delimiter.join(input)
        super().write_lines(input)


from datetime import datetime
file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/data/'

class WriteFile(object):
    def __init__(self, file_name, writer):
        self.fh = open(file_path+file_name, 'a+')
        self.formatter = writer()


    def write(self, input):
        self.fh.write(self.formatter.format(input))
        self.fh.write('\n')


    def close(self):
        self.fh.close()


class CSVFormatter(object):
    def __init__(self):
        self.delim = ','

    def format(self, input):
        for idx, element in enumerate(input):
            if self.delim in element:
                input[idx] = f'"{element}"'
        return self.delim.join(input)


class LogFormatter(object):

    def format(self, input):
        dt = datetime.now()
        dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
        return f'{dt_str} {input}'
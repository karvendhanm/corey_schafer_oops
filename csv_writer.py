import csv
file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/data/'

myData = ['Tom', 'Smith', 'B']

csv_file = open(file_path+'log.csv', 'w')


with csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(myData)

print('writing complete')



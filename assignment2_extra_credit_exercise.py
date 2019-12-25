from assignment2_extra_credit import WriteFile, CSVFormatter, LogFormatter


writecsv = WriteFile('text.csv', CSVFormatter)
writelog = WriteFile('log.txt', LogFormatter)

writecsv.write(['a', 'b,2', 'c', 'd'])
writelog.write('this is a log message')

writecsv.write(['1', '2', '3', '4'])
writelog.write('this is another log message')

writelog.close()
writecsv.close()

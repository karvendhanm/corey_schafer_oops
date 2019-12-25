from assignment2_exe_sol import LogFile, DelimFile

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('this is a another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])



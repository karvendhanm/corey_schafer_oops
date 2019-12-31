import sys
from assignment_3 import ConfigDict
file_path = 'C:/Users/John/PycharmProjects/corey_schafer_oops/data/'

cd = ConfigDict(file_path+'config.txt')

cd['sql_query']='SELECT this FROM that WHERE condition'
cd['email_to']='me@mydomain.com'
cd['num_retries']=5
cd['name'] = 'karvendhan'
cd['age']=35

print(sys.argv)

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data: {}, {}'.format(key, value))

    cd[key] = value

else:
    print('reading data')
    for key in cd.keys():
        print('  {0} = {1}'.format(key, cd[key]))
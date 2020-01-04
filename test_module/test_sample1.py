# testing by substring matching -------------> py.test -k method2 -v
# running certain methods using markers -----------> py.test -m set2
# running multiple workers at the same time ---------> py.test -n 4
# to get the results in an xml file ---------> py.test test_sample1.py -v --junitxml='result.xml'

import sys
sys.path.append('../')

from file_folder.doubleit import double
import pytest

def test_double():
    assert double(19) == 38, 'double function testcase 1 failed'
    assert double(20) == 38, 'double function testcase 2 failed'

# Run test by markers
@pytest.mark.set1
def test_file1_method1():
    x=5
    y=6
    assert x+1 == y, 'test failed'
    assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set2
def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, 'test failed'
    assert x + 2 == y, 'test failed'




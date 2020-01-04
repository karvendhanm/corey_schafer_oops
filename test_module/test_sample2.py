# testing by substring matching -------------> py.test -k method2 -v
# running certain methods using markers -----------> py.test -m set2
# running multiple workers at the same time ---------> py.test -n 4

import pytest
import sys
sys.path.append('../')


@pytest.mark.set1
def test_file2_method1():
    x=5
    y=6
    assert x+1 == y,"test failed"
    assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set2
def test_file2_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
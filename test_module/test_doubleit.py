import sys
import pytest
sys.path.append('../')


from file_folder.doubleit import double

@pytest.mark.udemy
def test_doubleit_method1():
    assert double(19) == 38, 'method double fails'
    assert double(24) == 38, 'method double fails'

@pytest.mark.udemy
def test_doubleit_type():
    with pytest.raises(TypeError):
        double('Hello')



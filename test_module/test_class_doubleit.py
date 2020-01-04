import sys
import pytest
import shutil
import os

sys.path.append('../')

from file_folder import doubleit


@pytest.mark.udemy_class
class TestDoubleit(object):

    numbers_file_template = 'testnums_template.txt'
    numbers_file_testor = 'testnums.txt'

    def setup_method(self):
        shutil.copy(TestDoubleit.numbers_file_template, TestDoubleit.numbers_file_testor)

    def teardown_class(self):
        os.remove(TestDoubleit.numbers_file_testor)

    def test_doublelines(self):
        doubleit.doublelines(TestDoubleit.numbers_file_testor)
        old_vals = [int(line) for line in open(TestDoubleit.numbers_file_template)]
        new_vals = [int(line) for line in open(TestDoubleit.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val)*2

    def test_doubleit_method1(self):
        assert doubleit.double(19) == 38, 'method double fails'
        assert doubleit.double(24) == 38, 'method double fails'

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            doubleit.double('hello')


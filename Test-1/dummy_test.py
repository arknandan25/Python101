import pytest
# calling test script: pytest test_file_name.py
# specific test: py.test -k test_method3 -v    <- this is the main test command
# or : py.test -m three
# ipdb dosen't work in the test :(

def func(x):
    return x*1


def test_method1():
    assert func(1) == 1


def test_method2():
    assert func(100) == 1002

@pytest.mark.three
def test_method3():
    assert func(3) == 3

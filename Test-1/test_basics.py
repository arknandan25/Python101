from unittest import mock
from unittest.mock import MagicMock

from basics import calculator
from basics import ProductionClass

@mock.patch('basics.calculator')
def test_calculator(mock_calculator_call):
    mock_calculator_call.return_value = MagicMock(output=100)
    import ipdb
    ipdb.set_trace()
    print(mock_calculator_call.return_value)


def test_prod_method():
    prod_class_object = ProductionClass()
    # setting the method  of the class to a mock with its return value
    prod_class_object.prod_method = MagicMock(return_value=59)
    print(prod_class_object.prod_method())
    import pdb
    pdb.set_trace()
    assert prod_class_object.prod_method() == 59
    # prod_class_object.prod_method.assert_called()
# FAILED test_basics.py::test_prod_method - assert 59 == 590

# -> assert prod_class_object.prod_method() == 590
# (Pdb) prod_class_object
# <basics.ProductionClass object at 0x7f8d76059278>
# (Pdb) MagicMock(return_value=59)
# <MagicMock id='140245538158464'>
# (Pdb) MagicMock(return_value=59).return_value
# 59
# (Pdb) prod_class_object.prod_method
# <MagicMock id='140245547192560'>
# (Pdb) prod_class_object.prod_method.return_value
# 59
# (Pdb) prod_class_object.prod_method()
# 59

# ----

# Example of the difference between Mock and MagicMock class

# Note we have mocked the return type of the magic method str only for this mock
# thus for other inputs like 12 it gives a string of 12
# for str(mock) it returns what you defined as the return value
# >>> mock = MagicMock()
# >>> mock.__str__.return_value = "lolz"
# >>> str(12)
# '12'
# >>> str(mock)
# 'lolz'


# >>> from unittest.mock import Mock
# >>> mock = Mock()
# >>> mock.__str__ = Mock(return_value="rofl")
# >>> str(mock)
# 'rofl'
# >>> str(44)
# '44'

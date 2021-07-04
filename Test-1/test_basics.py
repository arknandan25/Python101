from unittest import mock
from unittest.mock import MagicMock

from basics import calculator


@mock.patch('basics.calculator')
def test_calculator(mock_calculator_call):
    mock_calculator_call.return_value = MagicMock(output=100)
    import ipdb
    ipdb.set_trace()
    print(mock_calculator_call.return_value)

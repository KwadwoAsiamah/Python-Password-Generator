import pytest
from unittest import mock
from PythonPasswordGenerator import generatePWD


@pytest.fixture()
def generatePWDMockInput(mockInpt, monkeypatch):
    """
    Mock input fixture function for the test functions
    """
    mockInput = mock.MagicMock(return_value=mockInpt)
    monkeypatch.setattr("builtins.input", mockInput)
    result = generatePWD()
    mockInput.assert_called()
    return (result, mockInput)


@pytest.mark.parametrize("mockInpt", ["abc"])
def test_userInputIsNotANumber(generatePWDMockInput):
    """
    Tests if the user input provided is not a number
    """
    assert generatePWDMockInput[0] is False


@pytest.mark.parametrize("mockInpt", [""])
def test_userInputIsEmpty(generatePWDMockInput):
    """
    Tests if the stripped input of the user is empty
    """
    assert isinstance(generatePWDMockInput[0], str) \
        and len(generatePWDMockInput[0]) == 8


@pytest.mark.parametrize("mockInpt", ["6"])
def test_userInputIsLessThan8(generatePWDMockInput):
    """
    Tests if the user input provided is a number but less than 8
    """
    assert generatePWDMockInput[0] is False


@pytest.mark.parametrize("mockInpt", ["8"])
def test_userInputIs8(generatePWDMockInput):
    """
    Tests if the user input provided is 8
    """
    assert isinstance(generatePWDMockInput[0], str) \
        and len(generatePWDMockInput[0]) == 8


@pytest.mark.parametrize("mockInpt", ["10"])
def test_userInputIsGreaterThan8(generatePWDMockInput):
    """
    Tests if the user input provided is greater than 8
    """
    assert isinstance(generatePWDMockInput[0], str) \
        and len(generatePWDMockInput[0]) == \
        int(generatePWDMockInput[1].return_value)

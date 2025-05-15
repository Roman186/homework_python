import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("PYTHON", "Python"),
    ("h", "H"),
    ("Lesson", "Lesson"),
    ("hello-world", "Hello-world"),
    ("123", "123")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (1.5, AttributeError),
    (123, AttributeError),
    (None, AttributeError),
    (True, AttributeError),
    ({}, AttributeError),
    ((), AttributeError)
])
def test_attribute_capitalize(input_str, expected):
    with pytest.raises(expected):
        string_utils.capitalize(input_str)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!@#%_", "!@#%_")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" test", "test"),
    ("   test", "test"),
    ("Lesson", "Lesson"),
    ("  okay  ", "okay  "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("    ", ""),
    ("", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (1.5, AttributeError),
    (123, AttributeError),
    (None, AttributeError),
    (["invalid"], AttributeError),
    (True, AttributeError),
    ({}, AttributeError),
    ((), AttributeError)

])
def test_attribute_trim(input_str, expected):
    with pytest.raises(expected):
        string_utils.trim(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("hello", "e", True),
    ("hello", "a", False),
    ("hello world", "lo", True),
    ("", "", True),
    (" ", " ", True),
    ("banana", "a", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("test", 123, TypeError),
    (12345, "1", TypeError),
    ("test", None, TypeError),
    (None, "a", TypeError),
    ({}, "a", TypeError),
    ([], "a", TypeError),
    ((), "a", TypeError),
    (True, "u", TypeError)
])
def test_attribute_contains(input_str, symbol, expected):
    with pytest.raises(expected):
        string_utils.contains(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("hello", "e", "hllo"),
    ("banana", "a", "bnn"),
    ("test", "x", "test"),
    ("", "a", ""),
    ("hello, world!", ",", "hello world!"),
    (" ", " ", "")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("test", 123, TypeError),
    (12345, "1", TypeError),
    ("test", None, TypeError),
    (None, "a", TypeError),
    ({}, "a", TypeError),
    ([], "a", TypeError),
    ((), "a", TypeError),
    (True, "u", TypeError)
])
def test_attribute_delete_symbol(input_str, symbol, expected):
    with pytest.raises(expected):
        string_utils.delete_symbol(input_str)


@pytest.mark.negative
def test_delete_symbol_empty():
    assert string_utils.delete_symbol("test", "") == "test"

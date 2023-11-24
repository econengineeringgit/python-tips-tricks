# Testing in Python

## Introduction

Testing is an important part of software development. It is a way to ensure that the code is working as expected. It is also a way to ensure that the code will continue to work as expected when it is modified.

There are many different types of tests. The most common types are unit tests, integration tests, and end-to-end tests. Unit tests are used to test individual functions or classes. Integration tests are used to test how different parts of the code work together. End-to-end tests are used to test the entire system.

## Unit testing

Unit testing is a software development process in which the smallest testable parts of an application, called units, are individually and independently scrutinized for proper operation. Unit testing can be done manually but is often automated.

## Testing frameworks

There are many different testing frameworks available for Python. The most popular ones are:

- [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://docs.pytest.org/en/latest/)

## unittest

The unittest module is a built-in Python module that allows you to write test cases for your applications. It provides a set of tools for constructing test cases and running them.

### Example

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
```

### Running tests

```bash
python -m unittest test_module1 test_module2

python -m unittest test_module.TestClass
```

## pytest

Pytest is a testing framework for Python. It is more powerful than the built-in unittest module and has a simpler syntax. It is alsw backwards compatible with unittest.

### Example

```python
import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

### Adventages over unittest

- No boilerplate code
- No need to subclass anything
- No need to call any assert method: built-in assert statement is enough

### Fixtures

Fixtures are functions that are run before each test function to set up a test environment. They are used to create objects that are needed for testing.

```python

import pytest

@pytest.fixture
def my_fixture():
    return 42

def test_my_fixture(my_fixture):
    assert my_fixture == 42
```

### Parametrization

Parametrization is a way to run the same test with different inputs. It is useful when you want to test a function with different inputs.

```python

import pytest

@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(input, expected):
    assert eval(input) == expected
```

### Running tests

```bash
pytest

```

## TDD

Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved to pass the new tests, only. This is opposed to software development that allows software to be added that is not proven to meet requirements.

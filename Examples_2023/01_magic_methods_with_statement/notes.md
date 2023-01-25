# Object oriented programming

Source: Corey Schafer, [Youtube](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc),
[GitHub code](https://github.com/CoreyMSchafer/code_snippets/tree/master/Object-Oriented)

* Everything is an 'Object' in python
* We can create own objects, 'classes'
* In class:
  * function -> method
  * variable -> attribute

* Class <-> instance of a class is not the same.
  * The class itself is a blueprint, a template for generating instances.
  * class variable vs. instance variable

* 'self' argument:
  * The instance itself
  * passed automatically

* __init__(self)
  * super() [Detailed video on super](https://www.youtube.com/watch?v=X1PQ7zzltz4)

## Part 2

[Python docs: Special methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)

### Text representation

When we call the print statement, Python first looks for the __str__ method defined in your class before falling back on the __repr__ method.

* __repr__
* __str__

### Math

[Python docs: Numeric types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

* __add__
* __sub__
* __mul__
* __truediv__
* ...

### Context manager

[RealPython article](https://realpython.com/python-with-statement/)

### Alternative constructor

### Getter_setter

@property

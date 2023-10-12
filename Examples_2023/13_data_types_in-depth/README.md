# In-depth look into Python datatypes (1)

## Python data model

* Python data model is a description of Python as a framework
* It formalizes the interfaces of the building blocks of the language itself, such as sequences, iterators, functions, classes, context managers and so on
* It is based on the so called **special methods** (or **magic methods**)
* The Python interpreter invokes special methods to perform basic object
operations, often triggered by special syntax.
* Special methods are always spelled with leading and trailing double underscores

Examples:

```python

__init__ # constructor
__repr__ # representation ()
__str__ # string representation (print)
__add__ # addition

__len__ # length
__iter__ # iteration
__getitem__ # indexing
__contains__ # membership
```

Usage of special methods:

```python

len(my_object) # calls my_object.__len__()
my_object[0] # calls my_object.__getitem__(0)
my_object in my_collection # calls my_collection.__contains__(my_object)
for item in my_object: # calls iter(my_object), which in turn calls my_object.__iter__()
```

Resources:

<https://www.fluentpython.com/extra/internals-of-sets-and-dicts/>
<https://pythontutor.com/>

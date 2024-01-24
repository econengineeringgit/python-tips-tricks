# Refactoring example

At this occasion we'll try out the "Live Share" extension of VS Code. This extension allows us to share our code with other people and work on it together.

## What is refactoring?

Refactoring is the process of changing a software system in such a way that it does not alter the external behavior of the code yet improves its internal structure. It is a disciplined way to clean up code that minimizes the chances of introducing bugs. In essence when you refactor you are improving the design of the code after it has been written.

## Live Share session

We'll start a Live Share session and refactor the code together. The goal is to make the code more readable and maintainable.

## Issues

- [ ] The code is not readable
- [ ] Folder dependent
- [ ] Empty except block
- [ ] No docstrings
- [ ] Unnecessary comments
- [ ] Unnecessary imports
- [ ] Wrong variable names
- [ ] Wrong function names
- [ ] Duplicate code
- [ ] No proper data structures
- [ ] Too many indentation
...

## Input file

We'll use the `phonebook.txt` file as input. It contains the following data:

```csv
Zsuzsanna Halász; +36 77 810-8668; Tapolcahalasi utca 8., H-1956 keresztkövesd
Nóra Sipos; (06)08/736-8459; Petőfi sándor utca 107., H-9082 Budapest
Péter Bakos; 76/326 1838; Dunakeszii utca 63., H-7855 Székesfehérvár
Éva Takács; +36 10 139-1859; Kunhídi utca 243., H-2993 ráctamásidevecser
```

The [original code](orig_code.py) has a lot of issues. We'll try to fix them together.

## Refactored code

The [refactored code](refactored_code.py) is much more readable and maintainable. It is also folder independent, so it can be used in any folder.

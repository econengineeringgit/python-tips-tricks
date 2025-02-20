# Environments for python

A virtual environment is a Python tool for **dependency management and project isolation**. They allow Python site packages (third party libraries) to be installed locally in an isolated directory for a particular project, as opposed to being installed globally (i.e. as part of a system-wide Python). \
[Source](https://towardsdatascience.com/virtual-environments-104c62d48c54)

## Adventages of using virtual environments

* Dependency issues: different package version for different projects.
* Installation without admin rights
* Keep a clean global `site-packages` folder
* Safely store credentials

## Conda environments

@Mátyás

## `venv` vs `virtualenv`

### `virtualenv`

* Python2 and Python3
* Not standard library

### `venv`

* Python3
* Standard library

---

* Activate (PS, cmd, bash ...)
* Deactivate
* Use the python path inside
* The python version used with which the environment is created

## Requirement files

```bash
pip freeze > requirement.txt
```

### Using git

Never commit the environment!\
Commit the `requirement.txt` file!

## Environmental variables

```python
import os
from getpass import getpass

# Method1: get pw from user
pw = getpass("Enter password...")

# Method2: load from environmental variable
pw = os.getenv("MY_SECRET_PASSWORD")
```

## Possible issues

* Copy-paste the project, including the "venv"
* `where python` or `which python` to see the interpreter path
*

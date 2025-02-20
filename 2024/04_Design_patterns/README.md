# Design Patterns

Short introduction of the most common design patterns in Python.

🎥 Video recording

 > Q:\08_DOCS\005_Oktatás_Kurzus\01_ECON\003__PythonTipsAndTricks__\VIDEO\2024_06_27_Design_Patterns.mp4

## Factory
When the script has multiple functions with the same input but based on different inputs (variables) it is decided which one to call, create a different function that gets these variables and decides itself when to use which function

### Exmaple
[generator.py](generator.py) used in [main.ipynb](main.ipynb)

## Singleton
When the script has a class that is needed throughout the whole script, but don't want to recreate it because of the lack of inputs or simply only one must exist.

### Example
[singleton.py](singleton.py) used in [main.ipynb](main.ipynb)

## Bridge
When a class calls a function and that function should be changeable for example validating a simulation the input is always the same the simulation itself, but the function can be different

### Example
[bridge.py](bridge.py) used in [main.ipynb](main.ipynb)

## MVC (Model-view-controller)
This is a structural design pattern that gives the programmer a system of files, where and how to put new code into the tool or where it can be found.<br>

The rules are simple:
- **Model** holds the information about the used 'classes'
- **View** should contain user interfaces, e.g.: TUI(Terminal-user-interface), GUI (Graphical-user-interface) webapps, ...
- **Controller** stores the logic of the tool

**Model** communicates with outside tools like databases, jsons and classes are created from them
**View** communicates with the **Controller** only, no exception, by default the **View** should never touch **Model**s only through the **Controller**. This way, the **View** is doing only what is available in the **Controller** and no code duplication will happen.
**Controller** communicates with the **Model**, it gets request from the **View** and sends the wanted information back.

### Example
[mvc.py](mvc.py)

## Plugin
This is also a structural design pattern that lets the code being expandable easily, meaning just copying a script with the wanted function names or having an additional config that tells the code what is the 'entry point'

In the given example there is a [**JSON**](plugin/plugin.json) file that holds new scripts path and the tool looks for ['ExtraTester'](plugin/plugs/extra.py) class in these moduls (it can be expanded that not only 'ExtraTester' name is allowed) and runs the 'test' method inside that class also.

### Example
[Plugin](plugin/plugin.py)

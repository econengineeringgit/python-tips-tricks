# Refactoring: Simple GUI application

We have a working code, but is it ready?
What are the next steps? How can we make it better? Let's see some tips and tricks.

## Covered topics

- Imports
- Line length
- Typing
- Separation of responsibilities
- Extracting methods
- (Naming)

🎥 Video recording

 > Q:\08_DOCS\005_Oktatás_Kurzus\01_ECON\003__PythonTipsAndTricks__\VIDEO\2025_02_20_Refactoring_example.mp4

# Refactor basics

The original code (the non-refactored) can be found in the `old` folder.<br>
The refactored version is in the `new` folder.

## What does the program do?

Opens a GUI where we can add persons' data to a json file, the gui can show those persons and filter them.

## Running

Create a virtual environment and install the requirments.txt, then<br>
`python new/main.py`<br>
or<br>
`python old/main.py`

## What is the issue with `old` version?

* Line length (more than 80-100 chars)
* No \_\_name\_\_ == "\_\_main\_\_" used
* Everything is in **one** file! What actually?
    * Start of the program
    * GUI
    * The logic for adding, reading and saving `Person`
    * The `Person` is just a dictionary

## What are the changes?

There is a system design for most of the GUIs: **MVC** (Model - View - Control)<br><br>
`Model` defines the objects of our program this time the `Person`.<br>
`View` is the GUI itself.<br>
`Control` handles the communication between `View` and `Model`.<br><br>

In the end it is not just a design for GUIs but can also work for Webapps, since the website we are watching is giving the look,<br>
the backend is the control and the model is the database where the data is mostly hold.

### Seperate the individual functions of the program

* GUI -> Shows us a window and displays Person
* Person -> Make it a class for better understanding
* Person Managing -> If we move logic from the GUI this is what we get
* Create config for better handling of static json path

## Final thoughts

This refactoring is not the best, may not suit for everyone. But this way the code is seperated and easy to adding functionality, finding bugs.<br>
It may require more 'learning' for the first time reading it, but if we start off like this it is much easier to work with it.<br>
<br>
The message of the refactor could be two point at the end:

* D.R.Y. -> Don't Repeat Yourself
* Seperation -> A piece of code (function, method, class) should only have **`1`** functionallity that is in it's name.
<br><br>
Also, even if you are not going to publish the code or only you will use your code for 100% even then, <br>
**write** `requirments.txt` for best compatibility, because if you move the directory the venv will not work anymore and must set up a new one.

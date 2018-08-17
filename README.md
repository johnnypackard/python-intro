# Introduction to Python
[Johnny Python's Flying Circus](https://github.com/johnnypackard/python-intro)

## About
Python is a programming language that lets you work more quickly and integrate your systems more effectively.

Learn more at: https://www.python.org/

Fun fact! The language is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles. Making references to Monty Python skits in documentation is not only allowed, it is encouraged!

## Setup
1. Install Homebrew by opening `Terminal` and run
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install Python 3:
```
$ brew install python3
```

### Choose IDE
There are many great IDEs specifically built for Python; you can find out more [here](https://www.techbeamers.com/best-python-ide-python-programming/). 

Because I'm using Visual Studio Code, I used this tutorial to get started with the required (and optional, yet good to use) packages:
[Python on VSC](https://code.visualstudio.com/docs/python/python-tutorial).

## Start VS Code in a project folder
In `Terminal`, create an empty folder called "hello", navigate into it, and open VS Code (`code`) in that folder (`.`) by entering the following commands:
```
mkdir hello
cd hello
code .
```

Because Python is an interpreted language, you must tell VS Code which interpreter to use.
From within VS Code, select a Python 3 interpreter by opening the **Command Palette** (`⇧⌘P`), start typing the **Python: Select Interpreter** command to search, then select the command. You can also use the **Select Python Environment** option on the Status Bar if available.

## Build your site
Now that you have Python 3 installed, you are ready to create and explore your first Python-based web site.

1. Open your new, previously created `hello` folder, and create a new file named `hello.py`. You'll notice it automatically opens in the editor.

2. Enter the following source code:
```
msg = "Hello World"
print(msg)
```
3. Right-click on your file and select **Run Python File in Terminal**

4. The command opens a terminal panel in which your Python interpreter is automatically activated, then runs `python3``hello.py`(macOS/Linux) or `python hello.py` (Windows)

5. There are two other ways you can run Python within VS Code:
* Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. This command is very convenient for testing just a part of a file.

* Use the Python: Start REPL command to opens a REPL terminal for the currently selected Python interpreter. In the REPL you can then enter and run lines of code one at a time.

## Next steps
While the [Python](https://www.python.org/) web site includes detailed documentation, it can be overwhelming to go through with little experience to guide you.

The following resources are the ones that I have found most helpful:

- [The Hello World Program](https://thehelloworldprogram.com/python/) - This website is absolutely fantastic! There are in-depth articles explaining what Python is, as well as how to get started learning it.

- [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Programmers) - Great for the lazy and those who just need inspiration.  There are hundreds of themes from minimalist to super fancy, all ready to install and run with.  

- [Python Tutorial - Step-by-Step](https://www.techbeamers.com/python-tutorial-step-by-step) - This tutorial aims to teach all basic to advanced level Python programming concepts to a large number of aspirants in the most efficient way.

- [The Geek Blog - Python Examples on GitHub](https://github.com/geekcomputers/Python) - 
Here is more detailed information about scripts an amateur programmer has written. He created these programs as experiments to play with the language, and to solve problems for himself. There's a lot of great code references here!
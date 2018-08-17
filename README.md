# Introduction to Python
[Johnny Python's Flying Circus](https://github.com/johnnypackard/python-intro)

## About
Python is a programming language that lets you work more quickly and integrate your systems more effectively.

Learn more at: https://www.python.org/

*Fun fact! The language is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles. Making references to Monty Python skits in documentation is not only allowed, it is encouraged!*

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

## Use Flask to output to the DOM
"Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!"
You can learn more about [Flask here](http://flask.pocoo.org/).

#Install Flask
On your file system, create a project folder for this tutorial, such as hello_flask.

In that folder, use the following command (as appropriate to your computer) to create a virtual environment named "env" based on your current interpreter:

# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
`python3 -m venv env`

# Windows
`py -3 -m venv env`
Note: Use a stock Python installation when running the above commands. If you use python.exe from an Anaconda installation, you see an error because the ensurepip module isn't available, and the environment is left in an unfinished state.

1. Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.

2. In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Select Interpreter command:

#Opening the Command Palette in VS Code

The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select your virtual environment:

Selecting the virtual environment for Python

Run Python: Create Terminal from the command palette, which creates a terminal and automatically activates the virtual environment by running its activate script.

Note: on Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Shell to set "Command Prompt" or "Git Bash" as your default instead.

The selected environment appears on the left side of the VS Code status bar, and notice the "(venv)" indicator that tells you that you're using a virtual environment:

Selected environment showing in the VS Code status bar

#Install Flask in the virtual environment by running one of the following commands:

# macOS/Linux
`pip3 install flask`

# Windows
`pip install flask`
You now have an self-contained environment ready for writing Flask code.

#Create and run a minimal Flask app
1. In VS Code, create a new file in your project folder named app.py using either File > New from the menu, pressing Ctrl+N, or using the new file icon in the Explorer View (shown below).

2. New file icon in Explorer View

3. In app.py, add code to import Flask and create an instance of the Flask object. If you type the code below (instead of using copy-paste), you can observe VS Code's IntelliSense and auto-completions:

```
from flask import Flask
app = Flask(__name__)
```

4. Also in app.py, add a function that returns content, in this case a simple string, and use Flask's app.route decorator to map the URL route / to that function:

```
@app.route("/")
def home():
    return 'Hello, Flask!'
```

*Tip: you can use multiple decorators on the same function, one per line, depending on how many different routes you want to map to the same function.*

5. Save the app.py file (⌘S).

In the terminal, run the app by entering `python3 -m flask run` (MacOS/Linux) or `python -m flask run` (Windows), which runs the Flask development server. The development server looks for `app.py` by default. When you run Flask, you should see output similar to the following:

```
(env) D:\py\\hello_flask>python -m flask run
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

*If you see an error that the Flask module cannot be found, make sure you've run pip3 install flask (MacOS/Linux) or pip install flask (Windows) in your virtual environment as described at the end of the previous section.*

Also, if you want to run the development server on a different IP address or port, use the host and port command line arguments, as with `--host=0.0.0.0 --port=80.`

To open your default browser to the rendered page, Ctrl+click the [http://127.0.0.1:5000/](http://127.0.0.1:5000/) URL in the terminal.

#The running app in a browser

Observe that when you visit a URL like /, a message appears in the debug terminal showing the HTTP request:

Stop the app by using `Ctrl+C` in the terminal.

*Tip: If you want to use a different filename than app.py, such as program.py, define an environment variable named FLASK_APP and set its value to your chosen file. Flask's development server then uses the value of FLASK_APP instead of the default file app.py. For more information, see Flask command line interface.*


## Next steps
While the [Python](https://www.python.org/) web site includes detailed documentation, it can be overwhelming to go through with little experience to guide you.

The following resources are the ones that I have found most helpful:

- [The Hello World Program](https://thehelloworldprogram.com/python/) - This website is absolutely fantastic! There are in-depth articles explaining what Python is, as well as how to get started learning it.

- [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Programmers) - Great for the lazy and those who just need inspiration.  There are hundreds of themes from minimalist to super fancy, all ready to install and run with.  

- [Python Tutorial - Step-by-Step](https://www.techbeamers.com/python-tutorial-step-by-step) - This tutorial aims to teach all basic to advanced level Python programming concepts to a large number of aspirants in the most efficient way.

- [The Geek Blog - Python Examples on GitHub](https://github.com/geekcomputers/Python) - 
Here is more detailed information about scripts an amateur programmer has written. He created these programs as experiments to play with the language, and to solve problems for himself. There's a lot of great code references here!
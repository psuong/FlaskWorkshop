# Python setup

### Python on Unix and Linux
* By default, many distributions of these operating systems come with Python 2.7 installed.
* If by any means, you do not have python 2.7 installed, you can simply go to the [download page](https://www.python.org/downloads/release/python-2711/), download the correct version and install it.

### Setting Up Python on Windows
* Download Python 2.7.11 from [here](https://www.python.org/downloads/)
  * Out of the box Python should work automatically, once it's installed.

# Pip Setup & Installation

### Pip on Unix and Linux
* By downloading and installing Python version 2.7.9 or greater, `pip` should come automatically. (Make sure you stick with Python2, if you've accidentally downloaded Python 3.5, you will need to set up aliases!)
* However, if you cannot access `pip` through your terminal, head over to the `pip` page [here](https://pip.pypa.io/en/stable/installing/) and follow the instructions.

### Setting up `pip` on Windows
* If the version of Python you downloaded is version 2.7.9 or greater, by default you'll get `pip`. **Again make sure you downloaded Python 2.**
* A more convenient way to run `pip`, is to do it through your Command Prompt, although that requires some additional setup

#### Setting up `pip` through the Command Prompt
* Open up Command Prompt
  * Type the following: `setx PATH "%PATH%;<Drive-Letter>:\path\to\python\directory\Scripts"`
    *  This will add `pip` to your environment variables, so that you can use it on Command Prompt and install more modules!

### What is a Virtual Environment and why do we need them?
* Different package versions for each project, allows you to isolate dependencies

### Installing the Pip module 'virtualenv'    
* To install `virtualenv`, simply write `pip install virtualenv` in your terminal/Command Prompt.

### Creating and activating a virtualenv
* Unix-based operating systems (OSX and Linux)
  * In your project's directory simply type `virtualenv <name-of-directory>`. This will create a directory with whatever you named your virtualenv.
  * To activate a virtualenv, simply write in your terminal `source <name-of-directory>/bin/activate`; this will create an environment for you to work in through your terminal.

* Windows operating systems
  * The instructions to create a virtualenv on Windows is exactly the same as creating it on a Unix based operating system. Simply type `virtualenv <name-of-directory>` in your Command Prompt.
  * Activating a virtualenv in Windows is a tad different than Unix. Instead of going into the `bin` directory, go to the `Scripts` directory instead. For example: `<name-of-directory>\Scripts\activate.bat` would be the correct way to activate a virtualenv on Windows.

# DEMO TIME

### How to use
```sh
virtualenv <name> #create
source <name>/bin/activate #change into the virtualenv

which python #check path with

deactivate #exit
```

### Packages that you will need
```sh
pip install Flask
pip install Flask-SQLAlchemy
```


> Remember to put your virtualenv in the ignore file on version control!

### To manage several virtual environments 
* Install ```virtualenvwrapper``` to better manage virtual environments

### More info
* **Installing pip** http://python-packaging-user-guide.readthedocs.org/en/latest/installing/#creating-virtual-environments


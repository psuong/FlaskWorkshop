# Python setup

### Getting Python On Unix (OSX and Linux Distros)
* Many Unix OS come with Python by default

### Setting Up Python on Windows
* Download Python 2.7.11 from [here](https://www.python.org/downloads/)
  * Out of the box Python should work automatically, once it's installed.

### Download pip, Python's package manager
* Once you have pip, install virtualenv
* Required tools for Python development

### Setting up pip on Windows
* If the version of Python you downloaded is version 2.7.9 or greater, by default you'll get pip
* A more convenient way to run pip, is to do it through your Command Prompt, although that requires some additional setup
* Setting up Pip through the Command Prompt
  * Open up Command Prompt
  * Type the following: `setx PATH "%PATH%;C:\Python27\Scripts"`
    *  This will add `pip` to your environment variables, so that you can use it on Command Prompt and install more modules!

### What is a Virtual Environment and why do we need them?
* Global vs. Isolated
* Different package versions for each project

### Installing the Pip module 'virtualenv'    
* To install `virtualenv`, simply write `pip install virtualenv` in your terminal (you may need root privileges!)

### Creating and activating a virtualenv
* Unix-based operating systems (OSX and Linux)
  * In your project's directory simply type `virtualenv venv`, you will create a directory called `venv`.
    * Note: You don't have to actually call your virtualenv "venv," you can call it whatever you'd like.
  * To activate a virtualenv, simply write in your terminal `venv/source/bin/activate`; this will create an environment for you to work in through your terminal.

* Windows operating systems
  * The instructions to create a virtualenv on Windows is exactly the same as creating it on a Unix based operating system. Simply type `virtualenv venv` in your Command Prompt.
  * Activating a virtualenv in Windows is a tad different than Unix. Instead of going into the `source` directory, go to the `Scripts` directory instead. For example: `venv\Scripts\activate.bat` would be the correct way to activate a virtualenv on Windows.

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


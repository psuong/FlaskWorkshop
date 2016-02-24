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
* #### Setting up Pip through the Command Prompt
  * Open up Command Prompt
  * Type the following: `setx PATH "%PATH%;C:\Python27\Scripts"`
    *  This will add `pip` to your environment variables, so that you can use it on Command Prompt

### What is a Virtual Environment and why do we need them?
* Global vs. Isolated
* Different package versions for each project

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


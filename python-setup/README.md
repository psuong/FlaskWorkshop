# Python setup

### Getting Python
* Many Unix OS come with Python by default
* Can be set up on Windows, just requires a bit more work

### Download pip, Python's package manager
* Once you have pip, install virtualenv
* Required tools for Python development

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

> Remember to put your virtualenv in the ignore file on version control!

### Advanced
* Install ```virtualenvwrapper``` to better manage virtual environments

### More info
* **Installing pip** http://python-packaging-user-guide.readthedocs.org/en/latest/installing/#creating-virtual-environments


## Learning **virtualenv** usage from the [guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```
virtualenv -h   # show help message

virtualenv venv  # create a folder named "venv" (the virtual env)

source venv/bin/activate  # activate the virtual environment

deactivate   # exit the virtual environment
```


## pip

usually use the 3 commands:

1. `pip install <package-name>`
2. `pip freeze > requirements.txt`    # export the current state of the environment packages
3. `pip install -r requirements.txt`   # install the same packages in a different environment

others pip usages:

* `pip -h`   # help message
* `pip search <package-name>  # search PyPI
* `pip show <package-name>  # show the info about the installed package

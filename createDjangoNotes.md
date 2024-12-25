# Initializing a django project

## About pyenv-win tool

pyenv-win is the windows version of pyenv,
it is usefull to manage multiple python versions on your machine
The instructor uses pyenv-win, but it is not strictly necessary.

## About pipx tool

pipx install each package in a isolated environment,
so its dependencies does not conflict with global installed packages.
The pipx make installed tool executable globally,
taking precedence over the same tool installed with pip
So it's higher in the PATH.
To consult the order in PATH these commands can be used:

    where black  # Windows
    which black # Linux/macOS

## Creating the project without pyenv

- Install python normally. apt or windows store
- Install pipx with:

        pip install pipx

- Add pipx to the PATH:

        python -m pipx ensurepath

- Restart your terminal
- Install poetry with:

        python -m pipx install poetry

- You can consult packages installed globally with:

        pip list

(pipx has to appear on the list)

- You can consult packages installed in their exclusive environments with:

        python -m pipx list

(poetry has to appear on the list)

- Create a new python project with:

        poetry new djangoproj

- Change to the created folder
- Create a virtual environment for the project with:

        poetry shell

- Go to command pallet and run "Select Python Interpreter" click on find and use poetry created environment.
  You can use the path given when the environment was created, for example:
  C:\Users\user\AppData\Local\pypoetry\Cache\virtualenvs\djangoproj-8I0EU_hx-py3.12

- Go to pyproject.toml and add a minimal version for django on dependencies, for example:
  [tool.poetry.dependencies]
  python = "^3.12"
  django = "^5.0.1"

- Run a terminal as admin and install dependencies, with:

        poetry install

- Verify if it was installed correctly, with:

        poetry run django-admin --version

- Delete subfolder with init file created by poetry
- Run command to initialize a django project

        poetry run django-admin startproject djangoproj .

- This will create some importante files:

  - manage.py: Used to run django commands
  - settings.py: Define all project configuration
  - urls: Define all endpoints/ routes
  - asgi: asynchronous entry points
  - wsgi: synchronous entry points

- Run server with:
  poetry run python .\manage.py runserver

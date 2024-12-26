# Making a new django project

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

- Run migrations, with:

        poetry run python .\manage.py migrate

This command applies all built-in migrations and any migrations for your installed apps (like auth, sessions, etc.).

Even if your project has no migrations folder (e.g., in your custom apps), Django’s core apps (auth, admin, contenttypes, etc.) come with pre-made migrations.

So, migrate will set up database tables for Django's built-in features (like users, groups, and permissions).

If you're working on a fresh project, this step ensures the admin system is functional.

- Create a superuser, with:

        poetry run python .\manage.py createsuperuser

- Run server, with:

        poetry run python .\manage.py runserver

- Go to server url/admin (http://127.0.0.1:8000/admin) on browser and log on admin panel of django

- Create a django app, with:

        poetry run python .\manage.py startapp app

It create some files:

 - admin.py to link models with admin panel
 - models.py to contain models that represent rows of database
 - app.py to configure the app and import from django project
 - tests.py for writing tests for the application
 - views.py for the writting application endpoints or logic for various urls
 - migrations folder to store database migrations if application makes ant database changes

- Add your app in INSTALLED_APPS array on settings.py

## Django App flow

User
|
V
Django Project (receive request)
|
V
urls.py on project folder
urls.py on app folder
(it looks for URL patterns)
|
V
views.py (passes the request to corresponding functions)
| A A
| | |
| | |
| | V
| | models.py (database interaction)
| V
| template.html (renders)
V
User (send response to the user)

In MVC Model/View/Controller terminology
Model = models.py
View = template.html
Controller = views.py

A good order to write the app is:
templates --> models --> views
UI -------------db---- navigation

if you already know the data you're going to have,
you can start with models

## After creating model, make migration and migrate

- After creating models in models.py, prepare migrations file, with:

        poetry run python .\manage.py makemigrations

  It create a migration file to initialize the database
  It will create a database file according to DATABASE in settings.py

- Apply migration file with:

        poetry run python .\manage.py migrate

  Remember that it will create a new database file,
  if it already exists, delete it first

- Database will be recreated, so it is need to create super user, with:

        poetry run python .\manage.py createsuperuser

- Restart server with proper command and go to admin panel
  You should be able to view your database schema and add/change data on database
  You may also see Authentication/User information

## Make html templates

- Make a template folder on django project root and subfolders for each app
- Set templates folder on settings.py TEMPLATES
  'DIRS': [BASE_DIR / 'templates'], # added templates directory
  BASE_DIR is the root directory of project
  APP_DIRS': True means that django will look also in apps folders

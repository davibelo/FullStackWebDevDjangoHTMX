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

        poetry run python manage.py runserver

- Run migrations, with:

        poetry run python manage.py migrate

This command applies all built-in migrations and any migrations for your installed apps (like auth, sessions, etc.).

Even if your project has no migrations folder (e.g., in your custom apps), Django’s core apps (auth, admin, contenttypes, etc.) come with pre-made migrations.

So, migrate will set up database tables for Django's built-in features (like users, groups, and permissions).

If you're working on a fresh project, this step ensures the admin system is functional.

- Create a superuser, with:

        poetry run python manage.py createsuperuser

- Run server, with:

        poetry run python manage.py runserver

- Go to server url/admin (http://127.0.0.1:8000/admin) on browser and log on admin panel of django

- Create a django app, with:

        poetry run python manage.py startapp app

It create some files:

    - admin.py to link models with admin panel
    - models.py to contain models that represent rows of database
    - app.py to configure the app and import from django project
    - tests.py for writing tests for the application
    - views.py for the writting application endpoints or logic for various urls
    - migrations folder to store database migrations if application makes ant database changes

- Add your app in INSTALLED_APPS array on settings.py

## Django App flow

User -->
Django Project (receive request) -->
urls.py on project folder
urls.py on app folder
(it looks for URL patterns) -->
views.py (passes the request to corresponding functions)
<--> models.py (database interaction)
<--> template.html (renders)
--> User (send response to the user)

In MVC Model/View/Controller terminology
Model = models.py
View = template.html
Controller = views.py

A good order to write the app is:
templates --> models --> views
UI --> db --> navigation

if you already know the data you're going to have,
you can start with models

## After creating model, make migration and migrate

- After creating models in models.py, prepare migrations file, with:

        poetry run python manage.py makemigrations

  It create a migration file to initialize the database
  It will create a database file according to DATABASE in settings.py

- Apply migration file with:

        poetry run python manage.py migrate

  Remember that it will create a new database file,
  if it already exists, delete it first

- Database will be recreated, so it is need to create super user, with:

        poetry run python manage.py createsuperuser

- Restart server with proper command and go to admin panel
  You should be able to view your database schema and add/change data on database
  You may also see Authentication/User information

## Make html templates

- Make a template folder on django project root and subfolders for each app
- Set templates folder on settings.py TEMPLATES
  'DIRS': [BASE_DIR / 'templates'], # added templates directory
  BASE_DIR is the root directory of project
  APP_DIRS': True means that django will look also in apps folders

## Making forms

- Create a forms.py inside app folder

See example

## Cookies

After a user request, a cookie is served with the http response
If user make another request, the cookie is returned to the server,
making the server "remember" some information about the user

### CSRF Attacks

CSRF (Cross-Site Request Forgery) is a web attack where a malicious site tricks a user's browser into performing unintended actions on a trusted site where they are logged in, using their session cookies.

This exploits the trust the server has in the user's authenticated state. For example, an attacker could trigger a money transfer or account change without user consent.

Prevention includes using CSRF tokens, SameSite cookies, validating referer/origin headers, and requiring re-authentication for sensitive actions.

Implementing these measures on http POST, PUT, DELETE methods helps protect against unauthorized requests.

The GET method is considered safer because it does not request changes to the server's data; it only retrieves information. However, GET requests can still be exploited in CSRF attacks if sensitive actions are improperly handled via URLs or if sensitive data is exposed in query strings. Proper validation and security measures should still be applied to all HTTP methods to ensure comprehensive protection.

In django CSRF tolkens are enable by default, you just need to remember using it on forms with:
        {% csrf_tolken %}

## Escape feature

The Django framework includes robust built-in features for ensuring web application security, one of which is its automatic HTML escaping mechanism. This feature prevents cross-site scripting (XSS) attacks by escaping special characters in user-generated content before rendering it in templates. For example, characters like `<`, `>`, and `&` are converted to their HTML-safe equivalents (`&lt;`, `&gt;`, and `&amp;`), ensuring that any potentially harmful scripts are rendered as plain text rather than executable code. Developers can selectively bypass this behavior using the `safe` filter in Django templates, but this should only be done when the content is explicitly verified to be secure. By default, Django’s escaping functionality promotes safer web applications without requiring extensive manual intervention from developers.

in views.py:

    from django.shortcuts import render

    def example_view(request):
        context = {
            "unsafe_content": "<script>alert('This is unsafe!');</script>",
            "safe_content": "This is safe text.",
        }
        return render(request, "example_template.html", context)

in template.html:

        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Escaping Example</title>
        </head>
        <body>
            <h1>Escaped Content:</h1>
            <p>{{ unsafe_content }}</p>

            <h1>Unescaped Content (using safe filter):</h1>
            <p>{{ unsafe_content|safe }}</p>
        </body>
        </html>

## Django Filters

In Django, filters are used in templates to transform or modify the data being displayed. Filters are applied to variables in templates using the pipe (|) character. For example, {{ variable|filter_name }} applies the specified filter to variable. Django provides a wide range of built-in filters, such as lower (to convert text to lowercase), date (to format dates), default (to provide a fallback value), and safe (to mark content as safe from escaping).

Filters are a powerful way to manipulate data directly in templates without modifying your views or models, helping keep logic out of the template layer. Custom filters can also be created for specific needs using Django’s @register.filter decorator. However, it’s crucial to use filters like safe carefully to avoid security risks.

Django filters reference:
https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-filters

## Using docker

- Create a Dockerfile on the workspace folder
- Create .dockerignore file
- Run command to build image on django project folder

        docker build -t djangoproj .

    -t djangoproj: The -t flag tags the image with a name. In this case, the image is tagged as djangoproj.
    .: The dot at the end specifies the build context, which is the current directory. Docker will look for a Dockerfile in this directory to build the image.

OBS: When building for 2nd time, Docker will only build according to file changes, so it will build faster

### Optional test, not linking your local folder to the container

- Create the container, with:

        docker run -p 8005:8000 --name djangoproj djangoproj

    docker run: This command runs a Docker container.

    -dp: This option runs as daemon and publishes a container's port(s) to the host. It maps the host's port to a container's port.

    8005:8000: 8005 is the host machine's port. When you access localhost:8005 on your host machine, it will forward the request to the container's port. 8000 is the container's port. This is the port the application inside the container is listening on (commonly used for Django apps).

    --name djangoproj: it name the container djangoproj

    djangoproj on the end is the docker image created before.

- Run the a command on the running container to execute migrations and initiate database, with:

        docker exec djangoproj poetry run python manage.py migrate

    in this case after djangoproj is the name of the container

- List all containers on machine, with:

        docker ps -a

- Delete the container created for the test, with:

        docker rm djangoproj

### Running container with volume using local files and database

When using Docker for Django development, the poetry install command in the Dockerfile can overwrite critical files like migrations and the database. To prevent this and use your local files, you must mount a volume with local files and pass this to the container, as shown below:

- Run the command to create the container on project folder, with:

    1. **Bash (Mac/Linux):**

            docker run -dp 8005:8000 --name djangoproj -v "$(pwd):/code" djangoproj

    2. **PowerShell (Windows):**

            docker run -dp 8005:8000 --name djangoproj -v "$(Get-Location):/code" djangoproj

    3. **Git Bash (Windows):**

            docker run -dp 8005:8000 --name djangoproj -v "//$(pwd):/code" djangoproj

    4. **CMD (Windows Command Prompt):**

            docker run -dp 8005:8000 --name djangoproj -v "%cd%:/code" djangoproj

- After creating the container, it can be stopped with Ctrl+C or docker stop djangoproj.
    It can be restarted with:

        docker start djangoproj

    Container can be monitored on Docker Desktop

## Django debug toolbar

- Install django debug toolbar, with:

        poetry add -G dev django-debug-toolbar

    - poetry add: This command adds a dependency to your project using Poetry, a Python dependency management tool.
    - -G dev: This flag specifies that the dependency should be added to the dev dependency group (used only in development, not in production).
    - django-debug-toolbar: The package name for the Django Debug Toolbar.

    The Django Debug Toolbar package is added to your project's pyproject.toml file under the [tool.poetry.group.dev.dependencies] section.

    It will be available only in development environments when installed.

    After installing the package, you need to configure it in your Django project:

- Enable it on settings.py in debug mode:

        if DEBUG:
            INSTALLED_APPS += [
                "debug_toolbar",
            ]

            MIDDLEWARE += [
                "debug_toolbar.middleware.DebugToolbarMiddleware",
            ]

            INTERNAL_IPS += [

            ]

- Add debug toolbar in django proj urls.py
    if settings.DEBUG:
        urlpatterns += [
            path("__debug__/", include("debug_toolbar.urls")),
        ]

- It is necessary to build image and run docker container again

OBS: When building production image, change poetry install step to:

        poetry install --only main

## Create a custom migration

For example, if you want to automate the process of create a superuser, create a empty migration on your django app with:

        poetry run python manage.py makemigrations --empty app

It will create a empty custom migration on migration folder, you can rename it and change code to:

To apply all migrations run:

        poetry run python manage.py migrate

## Create a migration to set an user default in case that user was not in database prior to the user integration

In models.py a foreign key is created on main table (articles) to relate it to users table
After that, it is necessary to execute makemigration and migrate commands again to make it happen on database



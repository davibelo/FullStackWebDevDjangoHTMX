FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install gettext -y

RUN mkdir /code
WORKDIR /code

RUN pip install poetry
COPY poetry.lock pyproject.toml ./

# For development use:
RUN poetry install --no-root 
# --no-root option explanation:
# If you are running your Django project directly 
# (e.g., using python manage.py runserver), 
# the project does not need to be installed as a package. 
# The code is executed directly from the source files in the current directory.

# For production use:
# RUN poetry install --only main

# For production use:
# COPY . .
# not necessary for development 
# if you mount the project folder as a volume with a command like:
# PowerShell: docker run -dp 8005:8000 --name djangoproj -v "$(Get-Location):/code" djangoproj


EXPOSE 8000
ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
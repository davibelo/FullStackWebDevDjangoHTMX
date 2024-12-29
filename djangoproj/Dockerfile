FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN pip install poetry
COPY poetry.lock pyproject.toml ./

RUN poetry install
COPY . .

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
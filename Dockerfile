FROM python:3.11-alpine

EXPOSE 8000

RUN apk update && apk add python3-dev
WORKDIR /app

COPY ./pyproject.toml /app
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY . /app

# Start the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "2", "test_service.app:app"]

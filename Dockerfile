FROM python:3.11

WORKDIR /tibber-dev-test

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app app

CMD ["python", "-m", "fastapi", "run", "app/main.py", "--port", "80"]

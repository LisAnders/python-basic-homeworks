# сборка контейнера docker build . -t homework_03
# запуск контейнера docker run -it -p 8000:8000 homework_03
FROM python:3.10-buster

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
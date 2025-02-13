FROM python:3.10-slim-buster


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip3 install --upgrade pip -i https://mirror-pypi.runflare.com/simple
RUN pip3 install -r requirements.txt -i https://mirror-pypi.runflare.com/simple

COPY ./core .

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
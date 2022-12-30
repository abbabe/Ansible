# WEBAPP
FROM python:3.7-alpine
COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
ADD  . /app

EXPOSE 80

CMD python3 app.py
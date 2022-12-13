FROM ubuntu:latest

WORKDIR /opt/app
EXPOSE 5067
EXPOSE 8067
COPY requirements.txt ./
COPY . .

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3.10 python3-pip python3-gunicorn gunicorn -y
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/app
CMD [ "/usr/bin/gunicorn", "--bind", "0.0.0.0:5067", "wsgi:app" ]

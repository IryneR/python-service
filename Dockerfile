#from docker example
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


#FROM ubuntu:16.04
#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
#COPY ./requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip install -r requirements.txt
#COPY . /app
#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]

#FROM python:3
#WORKDIR /src/app
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
#CMD [ "python", "./app.py" ]




#from dockerhub
#FROM python:3
#WORKDIR /usr/src/app
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
#CMD [ "python", "./your-daemon-or-script.py" ]
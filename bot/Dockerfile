FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

RUN apt-get update && apt-get install -y \
    sudo

# Install dependencies
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8001

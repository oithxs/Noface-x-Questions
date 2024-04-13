FROM python:3.10
ENV PYTHONUNBUFFERED 1

# User
ARG USERNAME=dev
ARG GROUPNAME=dev
ARG UID=1000
ARG GID=1000

RUN mkdir /code

RUN apt-get update && apt-get install -y \
    sudo

# Create user
RUN groupadd -g $GID $GROUPNAME
RUN useradd -u $UID -g $GID -m $USERNAME

# Permissions
RUN chown -R $USERNAME:$GROUPNAME /code
RUN gpasswd -a $USERNAME sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER $USERNAME

# Install dependencies
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000

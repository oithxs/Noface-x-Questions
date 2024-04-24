FROM golang:1.22.2

WORKDIR /usr/src/app

ARG USERNAME=dev
ARG GROUPNAME=dev
ARG UID=1000
ARG GID=1000

RUN apt-get update && apt-get install -y \
    sudo nano tzdata;

# Create a group and user
RUN groupadd -g $GID $GROUPNAME
RUN useradd -u $UID -g $GID -m $USERNAME
RUN usermod -aG sudo $USERNAME
RUN echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN chown -R $USERNAME:$USERNAME /usr/src/app

USER dev

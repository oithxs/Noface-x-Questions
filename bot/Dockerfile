FROM python:3.10

ENV PYTHONUNBUFFERED 1

ARG USERNAME=pyuser
ARG GROUPNAME=pyuser
ARG UID=1000
ARG GID=1000
RUN mkdir /usr/src/app

RUN apt-get update && apt-get install -y \
    sudo nano;

# Create a group and user
RUN groupadd -g $GID $GROUPNAME
RUN useradd -u $UID -g $GID -m $USERNAME
RUN usermod -aG sudo $USERNAME
RUN echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN chown -R $USERNAME:$USERNAME /usr/src/app

USER $USERNAME

# Install dependencies
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt

EXPOSE 8001

CMD ["/bin/bash", "-c", "python3 main.py"]

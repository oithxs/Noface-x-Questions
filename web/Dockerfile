FROM node:21.7.3

WORKDIR /usr/src/app

ENV LANG="C.UTF-8"
ENV TZ="Asia/Tokyo"
ENV CI true

RUN apt-get update -y -qq && apt-get install -y -qq \
    sudo nano tzdata; \
    apt-get clean; \
    rm -rf /var/lib/apt-get/lists/*; \
    usermod -aG sudo node; \
    echo "node ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers;

COPY containerStart.sh /usr/local/bin/containerStart.sh

RUN chmod +x /usr/local/bin/containerStart.sh

USER node

EXPOSE 3000

CMD ["/bin/bash", "-c", "containerStart.sh"]

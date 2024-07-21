FROM debian:buster

RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib" >> /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y python3 python3-pip ffmpeg

RUN pip3 install --no-cache-dir pytube

WORKDIR /code

ADD index.py .



FROM python:3.10-alpine

COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt
COPY src /src

RUN pip3 install -r /requirements.txt &&\
    apk add git &&\
    chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

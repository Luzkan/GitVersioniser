FROM python:3.10-alpine

COPY entrypoint.sh /entrypoint.sh
COPY src /src
COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt
RUN apk add git
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

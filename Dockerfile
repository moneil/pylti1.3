FROM python:3.6.6-alpine3.7
RUN apk add --update \
    build-base libffi-dev openssl-dev \
    xmlsec xmlsec-dev
RUN apk upgrade && rm -rf /var/cache/apk/* ## upgrades the OS so that it will get clean scans in repos.
RUN pip install --upgrade pip ## gets rid of the pip version warning…
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY ./game /game
COPY ./configs /configs
EXPOSE 9001
CMD python app.py
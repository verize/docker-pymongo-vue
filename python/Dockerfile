FROM python:3.6.5-alpine3.7

LABEL maintainer="Gonzalo Plaza <gonzalo@verize.com>"

RUN apk add --no-cache \
  python3-dev \
  uwsgi-python3 \ 
  build-base \
  libffi-dev \
  openssl-dev

RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

RUN addgroup -S www-data && adduser -S -G www-data www-data 

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "uwsgi", "--socket", "0.0.0.0:5000", \
#               "--uid", "www-data", \
#               "--plugins", "python3", \
#               "--protocol", "http", \
#               "--wsgi", "wsgi:app" ]

EXPOSE 5000
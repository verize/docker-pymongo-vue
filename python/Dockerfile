FROM python:3.6.5-alpine3.7

LABEL maintainer="Gonzalo Plaza <gonzalo@verize.com>"

RUN apk add --no-cache \
  python3-dev \
  build-base \
  libffi-dev \
  openssl-dev

RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /app

EXPOSE 5000
CMD [ "python", "./app.py" ]
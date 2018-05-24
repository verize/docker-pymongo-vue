# Copyright 2018 Gonzalo Plaza
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM python:3.6.5-alpine3.7

LABEL maintainer="Gonzalo Plaza <gonzalo@verize.com>"

RUN apk add --no-cache \
  gcc \
	build-base \
	linux-headers \
  python3-dev \
  uwsgi-python3 \
  build-base \
  libffi-dev \
  openssl-dev \
  supervisor

RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

RUN addgroup -S www-data && adduser -S -G www-data www-data 

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.
COPY requirements.txt /usr/src/app/
RUN pip3 install -r /usr/src/app/requirements.txt

# add (the rest of) our code
COPY ./app /usr/src/app/
COPY app.ini /usr/src/app/
COPY app-entrypoint.sh /

RUN chmod 755 /app-entrypoint.sh
RUN mkdir -p /usr/src/app/build
RUN touch /usr/src/app/build/index.html
RUN echo "<h1>hello world</h1>" >> index.html

WORKDIR /usr/src/app/


EXPOSE 5000
CMD ["sh", "/app-entrypoint.sh"]
#CMD ["uwsgi", "--ini", "app.ini", "--uid","www-data","--gid","www-data"]
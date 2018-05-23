FROM nginx:1.14.0-alpine

LABEL maintainer="Gonzalo Plaza <gonzalo@verize.com>"

ADD nginx.conf /etc/nginx/
ADD app.conf /etc/nginx/conf.d/

RUN addgroup -S www-data && adduser -S -G www-data www-data

CMD ["nginx"]

EXPOSE 80
EXPOSE 443

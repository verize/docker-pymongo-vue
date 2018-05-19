FROM alpine:3.6

LABEL maintainer="Gonzalo Plaza <gonzalo@verize.com>"

RUN apk add --no-cache --update nginx
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

ADD nginx.conf /etc/nginx/
ADD app.conf /etc/nginx/conf.d/

RUN adduser -D -g '' -G www-data www-data

CMD ["nginx"]

EXPOSE 80
EXPOSE 443

FROM php:7.4-apache
LABEL maintainer="timeu.fo@gmail.com"
WORKDIR /var/www/html/ocusto
COPY . .
EXPOSE 8080:80
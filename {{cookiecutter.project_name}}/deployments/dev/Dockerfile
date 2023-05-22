FROM python:3.11-alpine

WORKDIR /var/www/app

COPY . .

RUN apk add --update --no-cache postgresql-client jpeg-dev \
    && apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    && pip install --upgrade pip

RUN pip install -r requirements/development.txt

CMD ["sh", "./entrypoint.sh"]

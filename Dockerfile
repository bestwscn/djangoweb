#基础库
FROM yaochenfeng/djangobase

ENV DJANGO_APP=djangoweb \
    DJANGO_VERSION=2.2.2 \
    APP_ENV=docker      \
    DJANGO_MANAGEMENT_ON_START="migrate --noinput;collectstatic --noinput"

COPY requirements.txt /usr/django/app
RUN chown -R django /usr/django/app \
    && pip install --no-cache-dir -r /usr/django/app/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY . /usr/django/app

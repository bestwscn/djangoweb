#基础库
FROM yaochenfeng/djangobase

ENV DJANGO_APP=djangoweb \
    DJANGO_VERSION=2.2.2 \
    APP_ENV=docker      \
    DJANGO_MANAGEMENT_ON_START="migrate --noinput;" \
    HEALTH_URL="localhost:8000/api"

#COPY requirements.txt /usr/django/app
#RUN chown -R django /usr/django/app \
#    && pip install --no-cache-dir -r /usr/django/app/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
COPY . /usr/django/app
HEALTHCHECK --interval=10s --timeout=2s --retries=12 CMD curl -f $HEALTH_URL || exit 1
FROM python:3.11.0-slim-bullseye AS run-image
ARG DEBIAN_FRONTEND=noninteractive

## update Debian and install runtime deps
RUN apt-get update &&\
    apt-get install -y \
            python3-pip \
            python3-dev \
            python3-cffi\
            python3-brotli\
            libpango-1.0-0\
            libpangoft2-1.0-0\
            default-libmysqlclient-dev\
            build-essential\
            nginx\
            vim\
            && apt-get autoremove &&\
            apt-get autoclean &&\
            rm -rf /var/lib//apt/lists/*

## Python and virtualenv settings
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 80

## Install Requirements
RUN python3 -m venv $VIRTUAL_ENV
RUN pip install --upgrade pip wheel pip-tools
## update requirements file with deployment requirement deps
COPY requirements.txt ./requirements.in
RUN echo "gunicorn" >> /requirements.in
RUN echo "mysqlclient" >> /requirements.in
RUN pip-compile ./requirements.in > ./requirements.txt \
    && pip-sync \
    && pip install -r ./requirements.txt

## Nginx configuration
COPY docker-files/nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

## Copy project folders
COPY . /app/

## Set workdir and call Django commands to makemigrations, migrate and collectstatic files.
WORKDIR /app/
# RUN python /app/manage.py makemigrations
RUN python /app/manage.py migrate --noinput
RUN python /app/manage.py collectstatic --noinput

# RUN chmod +x /app/docker-files/entrypoint.sh  
RUN chmod +x /app/docker-files/start.sh 
# start.sh expects as argurments the path to gunicorn_conf.py and the django application module.
ENTRYPOINT ["sh", "/app/docker-files/start.sh", "/app/docker-files/gunicorn_conf.py", "django_project.wsgi"]
# Use with: docker run -ti app-web-1:latest  
# at the command line.
# CMD ["/bin/bash"] 

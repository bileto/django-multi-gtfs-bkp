FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y binutils libproj-dev libsqlite3-mod-spatialite gdal-bin postgresql-client
RUN pip install "django>=4.2" "psycopg2"

RUN mkdir /code
RUN mkdir /feeds

COPY run_tests.py setup.py CHANGELOG.rst README.rst /code/
COPY multigtfs /code/multigtfs
COPY examples/explore /code/examples/explore

WORKDIR /code/examples/explore
RUN pip install -r /code/examples/explore/requirements.txt django_extensions django_nose Werkzeug

CMD ["/bin/bash", "/code/examples/explore/docker_run.sh"]

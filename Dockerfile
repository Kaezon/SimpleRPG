FROM python:3.6

ADD . /var/data/app
COPY ./entry-point /usr/local/bin/entry-point

WORKDIR "/var/data/app"

ENTRYPOINT ["entry-point"]

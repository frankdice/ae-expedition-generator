FROM python:3.7-alpine3.10

LABEL maintainer="Frank Dice <frank@babyvelociraptor.com>"

RUN apk update && apk upgrade
RUN apk add gcc python-dev linux-headers libc-dev

ENV rundir=/opt/ae-randomizer
RUN mkdir ${rundir}

COPY ./requirements.txt ${rundir}
WORKDIR ${rundir}
RUN pip3 install -r requirements.txt

RUN adduser -S flask

USER flask
WORKDIR ${rundir}
COPY ./ ${rundir}

ENTRYPOINT ["python"]
CMD ["main.py"]
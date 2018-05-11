FROM python:3.6
ENV PYTHONBUFFERED 1

RUN mkdir /pysite
WORKDIR /pysite

COPY . /pysite/
RUN pip3 install -r /pysite/requirements.txt

CMD ["/pysite/start.sh"]

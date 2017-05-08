FROM python

ADD . /opt/api-client
WORKDIR /opt/api-client

CMD python client.py

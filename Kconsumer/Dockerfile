FROM python:3.6.10-alpine3.11
WORKDIR /app
COPY consumer.py .
RUN pip3 install kafka-python
ENTRYPOINT ["python3","consumer.py"]
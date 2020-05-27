FROM python:3.6.10-alpine3.11
WORKDIR /app
ENV TOPIC="my-topic" \
		BOOTSTRAP="kafka1" \
		PORT="19092"
RUN pip3 install kafka-python
COPY producer.py .
ENTRYPOINT ["python3","producer.py"]
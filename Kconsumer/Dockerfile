FROM python:3.6.10-alpine3.11
WORKDIR /app
ENV TOPIC="my-topic" \
		GROUP="my-group" \
		BOOTSTRAP="kafka1" \
		PORT="19092" \
		CA="" \
		CERT=""
RUN pip3 install kafka-python
COPY . .
ENTRYPOINT ["sh", "entrypoint.sh"]
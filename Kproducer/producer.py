from kafka import KafkaProducer
import time
import os

topic = os.getenv('TOPIC').strip()
bootstrapServer=os.getenv('BOOTSTRAP').strip()
bootstrapPort=os.getenv('PORT').strip()


time.sleep(20)
producer = KafkaProducer(bootstrap_servers=['{}:{}'.format(bootstrapServer, bootstrapPort)])


for i in range(1000):
	message="this is message number: "+str(i)
	producer.send(topic,bytes(message, 'utf-8'))
	time.sleep(3)
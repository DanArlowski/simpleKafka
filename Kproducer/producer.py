from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

time.sleep(10)
producer = KafkaProducer(bootstrap_servers=['kafka1:19092'])


for i in range(1000):
	message="this is message number: "+str(i)
	producer.send('my-topic',bytes(message, 'utf-8'))
	time.sleep(3)
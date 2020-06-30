from kafka import KafkaProducer
import time
import os

topic = os.getenv('TOPIC').strip()
bootstrapServer=os.getenv('BOOTSTRAP').strip()
bootstrapPort=os.getenv('PORT').strip()
cert="/tmp/user-cert.crt"
ca="/tmp/ca.crt"
key="/tmp/key.pem"
#TODO: use producer user for producing

print ("values:", key,ca,cert, flush=True)
print ("connecting to {}:{}".format(bootstrapServer,bootstrapPort))

time.sleep(20)
producer = KafkaProducer(security_protocol='SSL', ssl_keyfile=key, ssl_certfile=cert, ssl_cafile=ca, bootstrap_servers=['{}:{}'.format(bootstrapServer, bootstrapPort)])


for i in range(1000):
	message="this is message number: "+str(i)
	producer.send(topic,bytes(message, 'utf-8'))
	time.sleep(3)
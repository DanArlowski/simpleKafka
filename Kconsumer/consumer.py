from kafka import KafkaConsumer
import time
import os 


## from ENV
topic = os.getenv('TOPIC').strip()
group = os.getenv('GROUP').strip()
bootstrapServer=os.getenv('BOOTSTRAP').strip()
bootstrapPort=os.getenv('PORT').strip()
print (topic, group, bootstrapServer, bootstrapPort, flush=True)
print("{}:{}".format(bootstrapServer, bootstrapPort), flush=True)
time.sleep(60)
consumer = KafkaConsumer(topic, group_id=group, bootstrap_servers=['{}:{}'.format(bootstrapServer, bootstrapPort)])
for message in consumer:
		print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value), flush=True)
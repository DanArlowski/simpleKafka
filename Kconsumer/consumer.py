from kafka import KafkaConsumer
import time
time.sleep(10)
consumer = KafkaConsumer('my-topic', group_id='my-group', bootstrap_servers=['kafka1:19092'])
for message in consumer:
		print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value), flush=True)
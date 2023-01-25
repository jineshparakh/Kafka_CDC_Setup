from kafka import KafkaProducer, BrokerConnection
from kafka.errors import KafkaError
import socket
from kazoo.client import KazooClient
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

if not zk.connected:
    # Not connected, stop trying to connect
    zk.stop()
    raise Exception("Unable to connect.")
# create a producer. broker is running on localhost
broker=BrokerConnection("localhost", 9092, socket.AF_INET)
print(broker)
producer = KafkaProducer(retries=5, bootstrap_servers=['localhost:9092'])
# define the on success and on error callback functions
def on_success(record):
    print(record.topic)
    print(record.partition)
    print(record.offset)

def on_error(excp):
    log.error(excp)
    raise Exception(excp)
# send the message to fintechexplained-topic
producer.send('fintechexplained-topic', {'key': 'value'}).add_callback(on_success).add_errback(on_error)
# block until all async messages are sent
producer.flush()



# To consume from fintechexplained-topic
consumer = KafkaConsumer('fintechexplained-topic',
                         group_id='my-group', enable_auto_commit=False,
                         bootstrap_servers=['localhost:9092'],
           value_deserializer=lambda m: json.loads(m.decode('ascii')))
for message in consumer:
    print(message.topic)
    print(message.partition)
    print(message.offset)
    print(message.key)
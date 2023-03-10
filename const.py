ZOOKEEPER_CONNECT_COMMAND = "zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties"
KAFKA_CONNECT_COMMAND = "kafka-server-start /opt/homebrew/etc/kafka/server.properties"
CONNECT_DISTRIBUTED_COMMAND = "connect-distributed $KAFKA_HOME/connect-distributed.properties"
LIST_KAFKA_TOPICS_COMMAND = "kafka-topics --bootstrap-server localhost:9092 --list"
CREATE_TOPIC_COMMAND = "kafka-topics --bootstrap-server localhost:9092 --create --topic "
DELETE_TOPIC_COMMAND = "kafka-topics --bootstrap-server localhost:9092 --delete --topic "
GET_ALL_CONNECTORS_COMMAND = "curl localhost:8083/connectors"
DELETE_CONNECTOR_COMMAND = "curl -X DELETE localhost:8083/connectors/"
HOST = "localhost"
ZOOKEEPER_PORT = 2181
KAFKA_PORT = 9092
CONNECT_DISTRIBUTED_PORT = 8083
NUM_RECORDS_UPSERTED = 20
SLEEP_SMALL = 3
SLEEP_MED = 10
SLEEP_LARGE = 20
COUCHBASE_USERNAME="Administrator"
COUCHBASE_PASSWORD="password"

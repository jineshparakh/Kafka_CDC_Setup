from kafka import KafkaConsumer


def getTopicRecords(topicName):
    consumer = KafkaConsumer(topicName, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], consumer_timeout_ms=1000)
    records = []
    for m in consumer:
        if m.value is None:
            continue
        records.append(str(m.value.decode().replace('"', "'")))
    consumer.close()
    return records

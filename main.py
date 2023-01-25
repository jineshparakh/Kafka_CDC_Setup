from zookeeperSetup import connectZookeeper
from kafkaSetup import connectKafkaServer
from upsertRecords import upsertRecords
import time
from topicManager import getAllTopics, createTopic, deleteTopic
from connectDistributed import connectDistributed, addConnector, deleteConnector
from consumer import getTopicRecords
from util import terminateProcess
import os
import const

if __name__ == "__main__":

    zookeeperProcess = connectZookeeper()
    kafkaProcess = connectKafkaServer()

    print("Printing all topics: ")
    print(getAllTopics())

    deleteTopic("__consumer_offsets")
    time.sleep(30)
    createTopic("__consumer_offsets")

    createTopic("CouchbaseCDCTopic")

    print("Printing all topics: ")
    print(getAllTopics())

    connectDistributedProcess = connectDistributed()

    result = addConnector(os.getcwd()+"/connect-distributed-properties.json")
    assert (result == True)

    upsertedRecords = upsertRecords(const.NUM_RECORDS_UPSERTED)
    time.sleep(const.SLEEP_MED)

    recordsFromKafka = getTopicRecords("CouchbaseCDCTopic")

    deleteConnector(os.getcwd()+"/connect-distributed-properties.json")

    deleteTopic("CouchbaseCDCTopic")
    # deleteTopic("__consumer_offsets")
    # time.sleep(30)
    # createTopic("__consumer_offsets")

    print("All topics: ")
    print(getAllTopics())

    terminateProcess(connectDistributedProcess)
    terminateProcess(kafkaProcess)
    terminateProcess(zookeeperProcess)
    print("Upserted Records: ")
    print(upsertedRecords)
    print("Records from Kafka: ")
    print(recordsFromKafka)

    print("len(upsertedRecords) is: " + str(len(upsertedRecords)))
    print("len(recordsFromKafka) is: " + str(len(recordsFromKafka)))

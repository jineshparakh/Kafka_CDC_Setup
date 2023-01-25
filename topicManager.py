import subprocess
import const
import time


def getAllTopics():
    getTopicsProcess = subprocess.run(
        const.LIST_KAFKA_TOPICS_COMMAND, shell=True, stdout=subprocess.PIPE)
    assert (getTopicsProcess.returncode == 0)
    return getTopicsProcess.stdout.decode()


def createTopic(topicName):
    print("Trying to create topic: " + topicName)
    createTopicProcess = subprocess.run(
        const.CREATE_TOPIC_COMMAND+topicName, shell=True, stdout=subprocess.PIPE)
    print("Created topic: " + topicName)
    print(createTopicProcess.stdout.decode())
    time.sleep(const.SLEEP_SMALL)
    return createTopicProcess.stdout.decode()


def deleteTopic(topicName):
    print("Trying to delete topic: " + topicName)
    deleteTopicProcess = subprocess.run(
        const.DELETE_TOPIC_COMMAND+topicName, shell=True, stdout=subprocess.PIPE)
    print("Deleted topic: " + topicName)
    print(deleteTopicProcess.stdout.decode())
    time.sleep(const.SLEEP_SMALL)
    return deleteTopicProcess.stdout.decode()

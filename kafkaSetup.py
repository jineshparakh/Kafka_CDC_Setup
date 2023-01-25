import os
import time
from util import isPortClosed, killProcessesOnPort
import const
import subprocess


def connectKafkaServer():
    if isPortClosed(const.HOST, const.KAFKA_PORT):
        print("Port " + str(const.KAFKA_PORT) +
              " already in use, trying to kill the process")
        killProcessesOnPort(const.KAFKA_PORT)

    kafkaStdoutFile = open(os.getcwd()+"/logs/kafkaStdout.log", 'w')
    kafkaErrorFile = open(os.getcwd()+"/logs/kafkaError.log", 'w')
    kafkaProcess = subprocess.Popen(const.KAFKA_CONNECT_COMMAND, shell=True,
                                    stdin=None, stdout=kafkaStdoutFile, stderr=kafkaErrorFile, close_fds=True)

    while isPortClosed(const.HOST, const.KAFKA_PORT) == False:
        print("Trying to connect to Kafka Server..")
        time.sleep(const.SLEEP_SMALL)

    print("Connected to Kafka Server")
    time.sleep(const.SLEEP_LARGE)

    return kafkaProcess

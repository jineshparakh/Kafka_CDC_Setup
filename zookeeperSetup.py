import os
import time
import subprocess
import const
from util import isPortClosed, killProcessesOnPort


def connectZookeeper():
    if isPortClosed(const.HOST, const.ZOOKEEPER_PORT):
        print("Port " + str(const.ZOOKEEPER_PORT)+ " already in use, trying to kill the process")
        killProcessesOnPort(const.ZOOKEEPER_PORT)

    zookeeperStdoutFile = open(os.getcwd()+"/logs/zookeeperStdout.log", 'w')
    zookeeperErrorFile = open(os.getcwd()+"/logs/zookeeperError.log", 'w')
    zookeeperProcess = subprocess.Popen(const.ZOOKEEPER_CONNECT_COMMAND, shell=True,
                                        stdin=None, stdout=zookeeperStdoutFile, stderr=zookeeperErrorFile, close_fds=True)

    while isPortClosed(const.HOST, const.ZOOKEEPER_PORT) == False:
        print("Trying to connect to Zookeeper..")
        time.sleep(const.SLEEP_SMALL)
    print("Connected to Zookeeper")
    time.sleep(const.SLEEP_MED)
    return zookeeperProcess
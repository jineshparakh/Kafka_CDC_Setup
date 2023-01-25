import os
import time
import json
import const
from util import isPortClosed, killProcessesOnPort
import subprocess


def connectDistributed():
    if isPortClosed(const.HOST, const.CONNECT_DISTRIBUTED_PORT):
        killProcessesOnPort(const.CONNECT_DISTRIBUTED_PORT)

    connectDistributedStdoutFile = open(
        os.getcwd()+"/logs/connectDistributedStdout.log", 'w')
    connectDistributedErrorFile = open(
        os.getcwd()+"/logs/connectDistributedError.log", 'w')
    connectDistributedProcess = subprocess.Popen(const.CONNECT_DISTRIBUTED_COMMAND, shell=True,
                                                 stdin=None, stdout=connectDistributedStdoutFile, stderr=connectDistributedErrorFile, close_fds=True)

    while isPortClosed(const.HOST, const.CONNECT_DISTRIBUTED_PORT) == True:
        print("Trying to connect to Connect Distributed..")
        time.sleep(const.SLEEP_SMALL)
    print("Connected to Connect Distributed")
    time.sleep(const.SLEEP_MED)
    return connectDistributedProcess


def addConnector(propertiesPath: str):
    file = open(propertiesPath)
    jsonContent = json.load(file)
    connectorName = jsonContent["name"]

    print("Trying to add connector: " + connectorName)
    addConnectorProcess = subprocess.run("curl -X POST -H Content-Type:\ application/json -d @" +
                                         propertiesPath+" localhost:8083/connectors", shell=True, stdout=subprocess.PIPE)

    assert (addConnectorProcess.returncode == 0)

    connectorResultString = subprocess.run(
        const.GET_ALL_CONNECTORS_COMMAND, shell=True, stdout=subprocess.PIPE).stdout.decode()
    print("Added connector: " + connectorName)
    return connectorResultString.find(connectorName) != -1


def deleteConnector(propertiesPath):
    file = open(propertiesPath)
    jsonContent = json.load(file)
    connectorName = jsonContent["name"]
    print("Trying to delete connector: " + connectorName)
    deleteConnectorProcess = subprocess.run(
        const.DELETE_CONNECTOR_COMMAND+jsonContent["name"], shell=True, stdout=subprocess.PIPE)
    assert (deleteConnectorProcess.returncode == 0)
    print("Deleted connector: " + connectorName)


def killConnectDistributed():
    z = os.system("kill -9 $(lsof -i:8083 | awk 'NR==2 {print $2}')")
    while os.system("nc -z localhost 8083") == 0:
        print("Trying to kill connect-distributed")
        time.sleep(const.SLEEP_SMALL)
    print("Killed connect-distributed")

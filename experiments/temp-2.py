
import const
import subprocess
import os
from util import isPortClosed
import time

zookeeperStdoutFile=open(os.getcwd()+"/logs/zookeeperStdout.log",'w')
zookeeperErrorFile=open(os.getcwd()+"/logs/zookeeperError.log", 'w')
zookeeperProcess = subprocess.Popen(const.ZOOKEEPER_CONNECT_COMMAND,shell=True,
             stdin=None, stdout=zookeeperStdoutFile, stderr=zookeeperErrorFile, close_fds=True)
# pid=subprocess.call(zookeeperCommand, shell=True)

# kafkaCommand=shlex.split(commands.KAFKA_COMMAND)
# pid2=subprocess.Popen(kafkaCommand, shell=True).pid
# while True:
#     print(isPortOpen("localhost", 2181))
#     time.sleep(5)
while isPortClosed("localhost", 2181)==True:
    print("Zookeeper not yet active")
    time.sleep(5)

kafkaStdoutFile=open(os.getcwd()+"/logs/kafkaStdout.log",'w')
kafkaErrorFile=open(os.getcwd()+"/logs/kafkaError.log", 'w')
kafkaProcess = subprocess.Popen(const.KAFKA_CONNECT_COMMAND,shell=True,
             stdin=None, stdout=kafkaStdoutFile, stderr=kafkaErrorFile, close_fds=True)

while isPortClosed("localhost", 9092):
    print("Kafka Server not yet active")
    time.sleep(5)
    continue
print("HERE")
time.sleep(50)

print(kafkaProcess.terminate())
# print(kafkaProcess.kill())
print(zookeeperProcess.kill())


print("Proc:")
print(zookeeperProcess.pid)
print(kafkaProcess.pid)
# while True:
#     continue
# print(pid2)



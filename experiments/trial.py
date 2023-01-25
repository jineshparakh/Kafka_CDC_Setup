import os
import shlex, subprocess
import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def checkIfPortIsOpen(host, port):
    return sock.connect_ex((host,port))==0
# output=os.system("zookeeper-server-start $KAFKA_HOME/zookeeper.properties")

# subprocess.Popen(f"zookeeper-server-start $KAFKA_HOME/zookeeper.properties", shell=True)
zookeeperCommand="zookeeper-server-start $KAFKA_HOME/zookeeper.properties &"
zookeeperCommand=shlex.split(zookeeperCommand)
print(zookeeperCommand)
proc=subprocess.Popen(zookeeperCommand,shell=True)
print(proc.pid)
print("KJDSHFk")

while checkIfPortIsOpen("localhost", 2181):
    print("2181 not binded")
print("2181 is binded")
print("kafka server start")
kafkaCommand="kafka-server-start $KAFKA_HOME/server.properties &"
kafkaCommand=shlex.split(kafkaCommand)
proc2=subprocess.Popen(kafkaCommand, shell=True)

while checkIfPortIsOpen("localhost", 9092):
    continue

print("9092 is binded")

output=os.system("kafka-topics --bootstrap-server localhost:9092 --list")
print(output)
# while True:
#     continue
# import asyncio

# async def run(cmd):
#     proc = await asyncio.create_subprocess_shell(
#         cmd,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)

#     stdout, stderr = await proc.communicate()

#     print(f'[{cmd!r} exited with {proc.returncode}]')
#     if stdout:
#         print(f'[stdout]\n{stdout.decode()}')
#     if stderr:
#         print(f'[stderr]\n{stderr.decode()}')

# asyncio.run(run('zookeeper-server-start $KAFKA_HOME/zookeeper.properties'))
# print("dslkf")
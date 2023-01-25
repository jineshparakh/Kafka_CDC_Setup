import socket
import os
import time
import subprocess
import const


def isPortClosed(host: str, port: int):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = (host, port)
    resultOfCheck = a_socket.connect_ex(location)
    a_socket.close()
    return resultOfCheck == 0


def terminateProcess(process: subprocess.Popen[bytes]):
    process.terminate()


def killProcess(process: subprocess.Popen[bytes]):
    process.kill()


def killProcessesOnPort(port: int):
    print("kill -9 $(lsof -i:"+str(port) + " | awk 'NR==2 {print $2}')")
    os.system("kill -9 $(lsof -i:"+str(port) + " | awk 'NR==2 {print $2}')")
    while isPortClosed("localhost", port):
        print("Trying to kill processes on port: " + str(port))
        time.sleep(const.SLEEP_SMALL)
    print("Processes on port: " + str(port) + " killed.")
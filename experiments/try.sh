#!/bin/sh
zookeeper-server-start  /opt/homebrew/etc/kafka/zookeeper.properties &
while ! nc localhost 2181
    do 
    echo "Doing"

done
echo "Done"
# echo "Done"

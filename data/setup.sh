#!/usr/bin/env bash

winpty docker exec spark-master apt-get update -y
winpty docker exec spark-master apt-get install python3-dev libmysqlclient-dev -y
winpty docker exec spark-master apt-get install python-pip -y
winpty docker exec spark-master pip install mysqlclient
winpty docker exec spark-master apt-get install python-mysqldb -y
winpty docker exec spark-worker apt-get update -y
winpty docker exec spark-worker apt-get install python3-dev libmysqlclient-dev -y
winpty docker exec spark-worker apt-get install python-pip -y
winpty docker exec spark-worker pip install mysqlclient
winpty docker exec spark-worker apt-get install python-mysqldb -y
winpty docker exec -it spark-master bin/spark-submit --master spark://spark-master:7077 --total-executor-cores 2 --executor-memory 512m /app/recommendation.py
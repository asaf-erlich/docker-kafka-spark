# Kafka With Spark Streaming

This repository contains a docker-compose.yml file which when started up creates a zookeeper backend, two kafkas, one intended to be used as a producer and one for use as a consumer, and spark available in a container for submitting streaming jobs.

## Educational Purpose

This repository was created to be used as part of a intro to data science class at Drexel University. Docker and docker-compose are being leveraged to reduce the technical burden requird to install all these components manually. Utilizing the docker-compose file in this repo students can understand how these components function together without wasting time setting them all up and hooking them together.

## Detail Summary

| Container | Image | Tag | Accessible |
|-|-|-|-|
| zookeeper | zookeeper | 3.6.1 | 172.25.0.11:2181 |
| kafka1 | wurstmeister/kafka | 2.12-2.2.0 | 172.25.0.12:9092 |
| kafka2 | wurstmeister/kafka | 2.12-2.2.0 | 172.25.0.13:9092 |
| spark | gettyimages/spark | 2.4.1-hadoop-3.0 | 172.25.0.14 |

# Quickstart

The easiest way to understand the setup is by diving into it and interacting with it.

## Running Docker Compose

To run docker compose simply run the following command in the current folder:

```
docker-compose up -d
```

This will run deattached. It will start all 4 containers.

To view the their status run

```
> docker-compose ps

Name                    Command               State                Ports
------------------------------------------------------------------------------------------
kafka1               start-kafka.sh                 Up         8080/tcp, 9092/tcp
kafka2               start-kafka.sh                 Up         8080/tcp, 9092/tcp
spark                bin/spark-class org.apache     Exit 127
zookeeper            /docker-entrypoint.sh zkSe     Up         2181/tcp, 2888/tcp,
```

If you want to see the logs, you can run:

```
docker-compose logs -f -t --tail=10 <container_name>
```

To see the memory and CPU usage (which comes in handy to ensure docker has enough memory) use:

```
docker stats
```

## Openining Shell Into Container

To open up a bash shell inside the spark container run the docker-compose exec command:

```
docker-compose exec spark bash
```

The current working directory is mounted in the /app folder inside the spark container. This will allow you to modify any files you move or copy into the repo's folder to appear inside the spark container.

## Running Sample Code

There are two samples of code included to test and try out publishing data onto a kafka topic and reading from it with spark.

### Publishing Data

Inside of the git repository there is a code sample to add the numbers 1 to 1000 onto a topic 'SAMPLE_TOPIC_NAME'. To view the code open the file create_topic_send_data.py. To run it follow these steps:

1. Open a shell inside the spark container (assumes the containers are up and running)
  ```
  docker-compose exec spark bash
  ```
1. Cd into the /app directory which has the volume pointing to the same directory as the root of the repository
  ```
  cd /app
  ```
1. Pip Install kafka-python
  ```
  pip install kafka-python
  ```
1. Execute the python code
  ```
  python create_topic_send_data.py
  ```

### Reading Data With Spark SQL

Also included is a code sample to read data from a topic using spark sql. To view the code open the file spark_read_from_topic_and_show.py. Also provided are two jar files that spark needs for spark sql and the kafka client. Because the volume is mounted into the /app folder all those files will be there to use. To run it follow these steps:

1. Open a shell inside the spark container (assumes the containers are up and running)
  ```
  docker-compose exec spark bash
  ```
1. Cd into the /app directory which has the volume pointing to the same directory as the root of the repository
  ```
  cd /app
  ```

1. Submit the python code to spark along with the jar files:
  ```
  spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 --jars kafka-clients-2.2.0.jar --driver-class-path kafka-clients-2.2.0.jar spark_read_from_topic_and_show.py
  ```

The output includes a lot of information but eventually you should expect to see

```
+---+-----+
|key|value|
+---+-----+
|  1|    1|
|  2|    2|
|  3|    3|
|  4|    4|
|  5|    5|
|  6|    6|
|  7|    7|
|  8|    8|
|  9|    9|
| 10|   10|
| 11|   11|
| 12|   12|
| 13|   13|
| 14|   14|
| 15|   15|
| 16|   16|
| 17|   17|
| 18|   18|
| 19|   19|
| 20|   20|
+---+-----+
only showing top 20 rows
```

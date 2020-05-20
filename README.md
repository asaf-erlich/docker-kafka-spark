# Kafka Spark Streaming With PySpark

This repository contains a docker-compose.yml file which when started up creates a zookeeper backend, two kafkas, one intended to be used as a producer andone for use as a consumer, and finally pyspark available in a file container for submitting streaming jobs through spark.

## Educational Purpose

This repository was created to be used as part of a intro to data science class at Drexel University. Docker and docker-compose are being leveraged to reduce the technical burden requird to install all these components manually. Utilizing the docker-compose file in this repo students can understand how these components function together without wasting time setting them all up and hooking them together.

## Detail Summary

| Container | Image | Tag | Accessible |
|-|-|-|-|
| zookeeper | zookeeper | 3.6.1 | 172.25.0.11:2181 |
| kafka1 | wurstmeister/kafka | 2.12-2.2.0 | 172.25.0.12:9092 |
| kafka1 | wurstmeister/kafka | 2.12-2.2.0 | 172.25.0.13:9092 |

# Quickstart

The easiest way to understand the setup is by diving into it and interacting with it.

## Running Docker Compose

To run docker compose simply run the following command in the current folder:

```
docker-compose up -d
```

This will run deattached. If you want to see the logs, you can run:

```
docker-compose logs -f -t --tail=10
```

To see the memory and CPU usage (which comes in handy to ensure docker has enough memory) use:

```
docker stats
```

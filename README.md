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

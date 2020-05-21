from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="172.25.0.12:9092"
)
producer = KafkaProducer(bootstrap_servers='172.25.0.13:9092')

TOPIC_NAME = 'SAMPLE_TOPIC_NAME'

existing_topics = admin_client.list_topics()

if TOPIC_NAME not in existing_topics:
    topic_list = [NewTopic(name=TOPIC_NAME, num_partitions=1, replication_factor=1)]
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

for i in range(1, 1001):
    key_bytes = bytes(str(i), encoding='utf-8')
    value_bytes = bytes(str(i), encoding='utf-8')
    producer.send(TOPIC_NAME, key=key_bytes, value=value_bytes)

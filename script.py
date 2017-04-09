from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
es = Elasticsearch([{'host': 'es', 'port': 9200}])


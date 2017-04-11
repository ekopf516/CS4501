from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time


def batch():
    ready = False
    while(not ready):
        try:
            KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
            ready = True
        except:
            print("checked")
            time.sleep(10)

    consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
    es = Elasticsearch([{'host': 'es', 'port': 9200}])

    with open('fixtures/db.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        for item in d:
            if item['model'] == 'my_project.book':
                some_new_listing = {'title': item['fields']['title'], 'author': item['fields']['author'], 'id': item['pk']}
                es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)

    while (True):
        for message in consumer:
            book = json.loads((message.value).decode('utf-8'))
            some_new_listing = {'title': book['title'], 'author': book['author'], 'id': book['id']}
            es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)



def main():
    batch()

if __name__ == '__main__':
    main()
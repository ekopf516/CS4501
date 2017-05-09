from kafka import KafkaConsumer
import json
import time


def batch():
    ready = False
    while(not ready):
        try:
            KafkaConsumer('user-book-pairs', group_id='pair-logger', bootstrap_servers=['kafka:9092'])
            ready = True
        except:
            time.sleep(10)

    consumer = KafkaConsumer('user-book-pairs', group_id='pair-logger', bootstrap_servers=['kafka:9092'])

    while (True):
        for message in consumer:
            group = json.loads((message.value).decode('utf-8'))
            username = group['user']
            book_id = group['book']
            log = open('access.log', 'a')
            log.write(username + "\t" + book_id + "\n")
            log.close()




def main():
    batch()

if __name__ == '__main__':
    main()
import pika
import json
auth=pika.PlainCredentials('qwer','1234') #auth info

connection = pika.BlockingConnection(pika.ConnectionParameters(
               '111.230.223.227',5672,'/',auth))   #connect to rabbit

channel = connection.channel()          #create channel


channel.queue_declare(queue='hello')      # decalre queue


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    print('name is',data['name'])
    print('message is',data['message'])


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

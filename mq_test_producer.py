import pika
import json
auth = pika.PlainCredentials('qwer','1234')  # save auth indo

connection = pika.BlockingConnection(pika.ConnectionParameters('111.230.223.227',5672,'/',auth))  #connect to rabbit

channel = connection.channel()   # create channel

channel.queue_declare(queue='hello')   # declare queue

message = {"name":"金平","message":"测试"}
message =json.dumps(message)
# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',routing_key='hello',body=message)  # the body is the msg content
print(" [x] Sent 'Hello World!'")
connection.close()

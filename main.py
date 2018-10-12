import itchat
import pika
import json

itchat.auto_login(enableCmdQR=2,hotReload=True)
# itchat.auto_login()
try:
    auth = pika.PlainCredentials('qwer', '1234')
    connection = pika.BlockingConnection(pika.ConnectionParameters('111.230.223.227', 5672, '/', auth))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
except:
    print('connect rabbitmq fail')


def callback(ch, method, properties, body):
    data = json.loads(body)
    user_name = data['name']
    message = data['message']
    info = itchat.search_friends(name=user_name)
    u_ids = []
    for item in info:
        u_ids.append(item['UserName'])
    for u_id in u_ids:
        try:
            itchat.send(message, toUserName=u_id)
        except:
            print('message send fail')
        else:
            print('send to:', user_name, '    with message:', message)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
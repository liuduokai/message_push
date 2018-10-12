import itchat
import time
import  threading


# itchat.auto_login(enableCmdQR=2)
itchat.auto_login()
info = itchat.search_friends(name='黄欣')
u_ids = []
for item in info:
    u_ids.append(item['UserName'])
for u_id in u_ids:
    print(u_id)
    # itchat.send(message, toUserName=u_id)
    # print('send to:', user_name, '    with message:', message)
print(info)

# def fun():
#     itchat.send('hello world', toUserName='filehelper')
#     print('send it')
#     timer = threading.Timer(10, fun)
#     timer.start()
#
#
# timer = threading.Timer(10,fun)
# timer.start()
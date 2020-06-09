"""
Домашнее задание будет заключаться в реализации простого эхо-чата с 
использованием JSON сообщений:
- клиент(ы) отправляет запрос (сообщение) серверу;
- сервер возвращает это же сообщение всем клиентам, кроме 
пославшего;
Клиент и сервер должны быть реализованы в виде отдельных скриптов, 
содержащих соответствующие функции.
Необходимо использовать несколько потоков на клиенте (один 
обрабатывает действие отправки сообщений, другой их получение).
ВАЖНО: Для обмена в качестве сообщений использовать JSON объекты. 
Пример JSON объекта представлен на следующем слайде.

2. Реализовать возможность отправки сообщений другим клиентам; 
(сделать можно различными способами, например, добавить адресата в 
JSON сообщение и реализовать соответствующее поведение на сервере)
"""

import socket
import time
import json


class JSONMessageEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__



class MessageBuilder:
    def __init__(self, msg):
        for key, val in msg.items():
            if isinstance(val, dict):
                sub_val = MessageBuilder(val)
                setattr(self, key, sub_val)
            else:
                setattr(self, key, val)

    def encode_to_json(self):
        return JSONMessageEncoder().encode(self)

    def get_object_of_json(self):
        return json.JSONDecoder(object_hook=MessageBuilder).decode(json_obj)


host = 'localhost'
port = 9090
clients = []
clients_names = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit_server = False
print(f"Server started")


while not quit_server:
    try:
        data, addr = s.recvfrom(1024)
        curr_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        decoded_msg = json.JSONDecoder(object_hook=MessageBuilder).decode(data.decode("utf-8"))
            

        if addr not in clients:
            clients.append(addr)
            clients_names.append(decoded_msg.user.name)
            #print(f"New member of chat: {addr} in {curr_time}")

        
        for i, client in enumerate(clients):
            adresat = decoded_msg.msg[1:decoded_msg.msg.find(" ")] if decoded_msg.action == "message" and decoded_msg.msg[0] == "@" else ""  
            if adresat:
                if addr != client and adresat == clients_names[i]:
                    s.sendto(data, client)
            elif addr != client:
                s.sendto(data, client)
                
                
    except Exception as ex:
        quit_server = True
        print(f"Server stopped, because {ex}")

s.close()

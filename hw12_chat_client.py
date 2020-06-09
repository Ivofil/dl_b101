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
"""

import io
import socket
import threading
import time
import json


shutdown = False
join = False


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


 

def receiving(client_name, sock):
    global shutdown
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                decoded_msg = json.JSONDecoder(object_hook=MessageBuilder).decode(data.decode("utf-8"))
                if decoded_msg.action == "message":
                    print(f"\n{decoded_msg.user.name}[{decoded_msg.user.status}]:: {decoded_msg.msg}")
                elif decoded_msg.action == "new_user":
                    print(f"Новый участник чата {decoded_msg.user.name}[{decoded_msg.user.status}]")


                    #print(data.decode("utf-8"))
                time.sleep(0.2)
        except Exception as ex:
            print(f"Что-то пошло не так: {ex}")
            shutdown = True


def sending(client_name, sock):
    global shutdown, join
    while not shutdown:
        if not join:
            #sock.sendto(f"[{client_name}] join chat!".encode("utf-8"), server)
            msg = MessageBuilder({"action": "new_user", "user": {"name": client_name, "status": "online"}})
            sock.sendto(msg.encode_to_json().encode("utf-8"), server)
            join = True
        else:
            try:
                message_client = input(f"Вы [{client_name}] :: ")
                msg = MessageBuilder({"action": "message", "msg": message_client,
                                     "user": {"name": client_name, "status": "online"}})
                if message_client:
                    sock.sendto(msg.encode_to_json().encode("utf-8"), server)
                time.sleep(0.2)
            except Exception as ex:
                print(f"Что-то пошло не так: {ex}")
                shutdown = True
    recv_thread.join()
    s.close()    


if __name__ == '__main__':
    user_name = input("Введите ваш логин: ")
    print("Внимание вы можете писать личные cообщения другим пользователям начиная сообщение так:\
          \n\"@имя_участника текст_сообщения\"")
    server = ('localhost', 9090)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('localhost', 0))

    recv_thread = threading.Thread(target=receiving, args=(user_name, s))
    recv_thread.start()
    sending(user_name, s)
    


    #msg1 = MessageBuilder({"response": 200, "alert": "default"})
    #name = "User123"
    msg2 = MessageBuilder(
        {"action": "presence", "time": time.ctime(), "user": {"name": name, "status": "online"}})
    #msg3 = MessageBuilder.create_presence_message(name="newUser")
    #msg4 = MessageBuilder.create_response_message(200, "default")

    #print(JSONMessageEncoder().encode(msg1))
    print(JSONMessageEncoder().encode(msg2))
    #print(JSONMessageEncoder().encode(msg3))
    #print(JSONMessageEncoder().encode(msg4))
    
    # Декодируем сообщение из json обратно в
    # можем обратиться по нужным атрибутам
    
    json_exemple_msg = JSONMessageEncoder().encode(msg2)
    decoded_obj = json.JSONDecoder(object_hook=MessageBuilder).decode(json_exemple_msg)
    print(decoded_obj.user.name)

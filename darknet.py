

import sys, time, socket, threading, os

os.system('clear')




banner = """
server, created by youtube.com/@darknet_off1cial
"""
host = '127.0.0.1'
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
darknet_bobo = []


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            uzdarkweb = darknet_bobo[index]
            broadcast(
                '{} chatdan chiketdi!\n'.format(uzdarkweb).encode('ascii'))
            darknet_bobo.remove(uzdarkweb)
            break


def receive():
    while True:
        client, address = server.accept()
        slowprint(
                  "Ulanildi".format(str(address)))
        client.send("NICKNAME".encode('ascii'))
        uzdarkweb = client.recv(1024).decode('ascii')
        darknet_bobo.append(uzdarkweb)
        clients.append(client)
        slowprint("foydalanuvchi: {}".format(uzdarkweb))
        broadcast("username: {} chatga qoshldi".format(
            uzdarkweb).encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print(banner)
slowprint("server ishga tushdi")
slowprint("client faylini ishga tushuring")
receive()


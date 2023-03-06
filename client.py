
import sys, time, socket, threading, os

os.system('clear')



banner = """
dasturchi: youtube: youtube.com/@darknet_off1cial
"""


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


print(banner)
slowprint("Serverga ulanilmoqda..." )

nickname = input("username yozing : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 4444
client.connect((server, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            slowprint("nimadir hato ! ")
            client.close()
            break


def write():
    while True:
        message = '{} -  >> {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()


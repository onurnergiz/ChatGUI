from socket import *
from threading import *

clients = []
names = []
def clientThread(client):
    bayrak = True
    while True:
        try:
            message = client.recv(1024).decode("utf8")
            if bayrak:
                names.append(message)
                print(message,"Bağlandı!")
                bayrak = False
            for c in clients:
                if c != client:
                    index = client.index(client)
                    name = names[index]
                    c.send((name + ":" + message).encode("utf8"))


        except:
            index = client.index(client)
            clients.remove(client)
            name=names[index]
            names.remove(name)
            print(name + "Sohbetten Çıktı!")

server= socket(AF_INET,SOCK_STREAM)


ip="127.0.0.1"
port=55555
server.bind((ip, port))
server.listen()
print("Server Dinlemede! ")

while True:
    client,address = server.accept()
    clients.append(client)
    print("Bağlantı Yapıldı!",address[0]+ ":" + str(address[1]))
    thread = Thread(traget=clientThread, args=client,)
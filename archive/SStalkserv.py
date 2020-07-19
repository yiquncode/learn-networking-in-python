# -*- coding: utf-8 -*-
import socket

HOST = ''
PORT = 8888
global serverSock

class ServerMain():
    def receiveMessage(self):
        self.serverSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSock.bind((HOST,PORT))
        self.serverSock.listen(5)
        self.buffer = 1024

        while 1:
            self.connection,address = self.serverSock.accept() #阻塞
            print 'A client from', address
            while 1:
                self.clientMsg = self.connection.recv(self.buffer)
                if not self.clientMsg:
                    continue
                else:
                    print 'Client ' + 'said: \r\n' + self.clientMsg
                    message = raw_input('> ')
                    self.connection.send(message)
def main():
    server = ServerMain()
    server.receiveMessage()
if __name__=='__main__':
    main()

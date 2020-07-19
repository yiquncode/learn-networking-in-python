# -*- coding: utf-8 -*-
from twisted.internet import protocol, reactor

HOST='localhost'
PORT=21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('> ') #阻塞
        if data:
            print '....send..... %s' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()
    def connectionMade(self): #这个方法连接成功时运行
        self.sendData()
    def dataReceived(self,data):
        print data
        self.sendData()
class TSClntFactory(protocol.ClientFactory):#管理连接事件
    protocol = TSClntProtocol#一旦连接建立，Protocol对象就接管下面的工作了，包括收发数据和决定是否关闭连接。
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason:reactor.stop()
reactor.connectTCP(HOST, PORT, TSClntFactory())#告知反应器建立一个TCP连接,通过TSClntFactory来管理连接
reactor.run()#启动反应器的事件循环,类似于WHILE TRUE 反应器将会一直运行，直到接到停止的通知

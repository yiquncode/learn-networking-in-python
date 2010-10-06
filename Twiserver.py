# -*- coding: utf-8 -*-
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host#transport包含了当前活动连接对象
        print 'from...:', clnt
    def dataReceived(self, data):
        print "ssss"#测试数据接收
        self.transport.write('[%s] %s' % (ctime(),data))
factory = protocol.Factory()#工厂,用于加工原材料
factory.protocol = TSServProtocol#员工就位
print 'waiting ...'
reactor.listenTCP(PORT, factory)
reactor.run()

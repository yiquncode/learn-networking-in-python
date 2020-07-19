# -*- coding: utf-8 -*-
from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = '' #留空监听所有IP
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):#继承基类SRH
	def handle(self):#重写HANDLE
		print '...from', self.client_address
		self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))
tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()

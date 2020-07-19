# -*- coding: utf-8 -*-
if __name__=='__main__':
    import socket
    #SOCK_STREAM(tcp) 套接字,面向连接
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8001))
    sock.listen(5)
    while True:
	    connection,address = sock.accept() #I'm in waiting
	    try:
		    connection.settimeout(5)
		    buf = connection.recv(1024) #缓冲区
		    if buf == '1':
		        connection.send('welcome to server')
		    else:
			    connection.send('please go out')
	    except socket.timeout:
		    print 'time out'
		    connection.close()

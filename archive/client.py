if __name__ =='__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',8001))
    import time
    time.sleep(6)
    sock.send('2')
    print sock.recv(1024)
    sock.close()
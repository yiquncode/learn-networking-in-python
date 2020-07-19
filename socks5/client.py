import socket
import struct

class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        print(f"Starting connection to {host}:{port}")
        self.sock.connect((host, port))
    
    def negotiate(self):
        self.sock.sendall(b"\x05\x02\x00\x01")
        data = self.sock.recv(1024)
        print('Received', repr(data))
    
    def request(self,domain,destport):
        req = b"\x05\x01\x00\x01"
        
        # Convert an IP address from its family-specific string format to a packed, binary format.
        ipaddr = socket.inet_aton(socket.gethostbyname(domain))
        req = req + ipaddr
        req = req + struct.pack(">H",destport)
        self.sock.sendall(req)

        # Get the response
        print(self.sock.recv(1024))
        self.sock.sendall(b"GET / HTTP/1.1\r\nHost: baidu.com\r\nUser-Agent: curl/7.64.0\r\nAccept: */*\r\n\r\n")
        print(self.sock.recv(1024))
    
    def close(self):
        self.sock.close()



socks5 = MySocket()
socks5.connect('127.0.0.1',4000)
socks5.negotiate()
socks5.request("baidu.com",80)
socks5.close()

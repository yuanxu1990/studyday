import socket
import hmac

client_key='yuan'.encode('utf-8')
ck=socket.socket()
ck.connect(('127.0.0.1',10090))

msg=ck.recv(1024)
h=hmac.new(client_key,msg)
client_digest=h.digest()
ck.send(client_digest)

ck.close()
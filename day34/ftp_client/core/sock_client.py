import socket
import json

class mysocketclient:
    def __init__(self):
       self.ck=socket.socket()
       self.ck.connect(('127.0.0.1', 10111))

    def mysend(self,msg):
        print(msg)
        json_data = json.dumps(msg)
        self.ck.send(json_data.encode('utf-8'))

import socketserver
import json
from core import views

class ftpserver(socketserver.BaseRequestHandler):
    def handle(self):
        json_msg=self.my_recv()
        op_str=json_msg['opertion']
        if hasattr(views,op_str):
            func_str=getattr(views,op_str)
            ret=func_str(json_msg)
            self.my_send(ret)
            # msg 获取 登录和用户名密码
            #{'username','password','operation'}  operation 指定操作方法名字


    def my_recv(self):#派生方法
        msg = self.request.recv(1024)
        # msg 获取 登录和用户名密码
        msg_str = msg.decode('utf-8')
        msg_json = json.loads(msg_str)
        return msg_json

    def my_send(self,msg):
        msg=json.dumps(msg).encode('utf-8')
        self.request.send(msg)


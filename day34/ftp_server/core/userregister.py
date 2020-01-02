from conf.settings import home_path,addr,code,disk_space
import os


class user:
    def __init__(self,name):
        self.name=name
        self.home=os.path.join(home_path,name)
        print(self.home)
        self.cur_path=self.home
        self.disk_space=disk_space
        self.file_size=0
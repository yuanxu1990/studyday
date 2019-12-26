import subprocess

#执行 shell 命令 正确的放在stdout 错误的放在stderr  PIPE是管道容器
res=subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print('stdout',res.stdout.read().decode('gbk'))
print('stderr',res.stderr.read().decode('gbk'))
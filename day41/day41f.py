'''
I/O模型
同步（synchronous）I/O
异步(asynchronous)I/O
阻塞(blocking)I/O
非阻塞(non-blocking)I/O

liunx 的network I/O

blocking IO        阻塞io
nonblocking IO     非阻塞io
IO multiplexing     io多路复用
signal driven IO     信号驱动io
asynchronous IO      异步io
由signal driver IO(信号驱动IO)在实际中并不常用，所有主要介绍其余四中IO model

等待数据准备(Waiting for the data to be ready)
将数据从内核拷贝到进程中(Copying the data form the kernel to the process)
io io模型的区别就是在以上两个阶段各有不同的情况

同步
  提交一个任务之后要等待这个任务执行完毕

异步
   直观提交任务，不等待这个任务执行完毕就可以做其他的事情

阻塞
    revc recvfrom accept

非阻塞


阻塞
  线程   运行状态--->阻塞状态--->就绪---->执行
非阻塞
   线程   运行完毕


'''


#阻塞io模型
# coding=gbk
# @file:01-多线程初探.py
# @data:2021/8/4 20:17
# Editor:clown
# 线程 进程
# 线程：执行单位  进程 ：执行单位  每个进程至少要有一个线程
'''单线程'''
# def func():
#     for i in range(10000):
#         print("func",i)
#
#
# #启动每个程序默认都会有一个主线程
# if __name__=="__main__":
#     func()
#     print("over!!!")
#     for i in range(10000):
#         print("main",i)


# for i in range(10000):
#     print(i)

from threading import Thread
def func():
    for i in range(10000):
        print("func",i)

if __name__=="__main__":
    # func()
    t=Thread(target=func) #创建线程并给线程安排任务
    t.start() #开始执行该线程 多线程状态为可以开始工作状态，具体执行时间 cpu
    for i in range(10000):
        print("main",i)

# class MyThread(Thread):
#     def run(self):   #固定的 -》当线程可以执行之后，被执行的就是run（）
#         for i in range(1000):
#             print("子线程",i)
#
#
# if __name__ == '__main__':
#     z=MyThread()
#     #z.run()#变成方法调用 -》单线程
#     z.start()#开启线程
#     for i in range(1000):
#         print("主线程", i)
#     z.run()
#     pass



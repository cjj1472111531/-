# coding=gbk
# @file:02-�����.py
# @data:2021/8/4 21:00
# Editor:clown
from multiprocessing import Process
from threading import Thread

# def func():
#     for i in range(10000):
#         print("�ӽ���",i)
#
# if __name__ == '__main__':
#     p=Process(target=func)
#     p.start()
#     for i in range(10000):
#         print("������",i)


# def func():
#     for i in range(10000):
#         print("�ӽ���",i)
#
# if __name__ == '__main__':
#     p=Process(target=func)
#     p.start()
#     for i in range(10000):
#         print("������",i)

def func(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    t1=Thread(target=func,args=("�ܽ���",))#���ݲ���������Ԫ��
    t1.start()
    t2=Thread(target=func,args=("������",))#���ݲ���������Ԫ��
    t2.start()
    for i in range(1000):
        print("������",i)

#https://www.51job.com/

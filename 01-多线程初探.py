# coding=gbk
# @file:01-���̳߳�̽.py
# @data:2021/8/4 20:17
# Editor:clown
# �߳� ����
# �̣߳�ִ�е�λ  ���� ��ִ�е�λ  ÿ����������Ҫ��һ���߳�
'''���߳�'''
# def func():
#     for i in range(10000):
#         print("func",i)
#
#
# #����ÿ������Ĭ�϶�����һ�����߳�
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
    t=Thread(target=func) #�����̲߳����̰߳�������
    t.start() #��ʼִ�и��߳� ���߳�״̬Ϊ���Կ�ʼ����״̬������ִ��ʱ�� cpu
    for i in range(10000):
        print("main",i)

# class MyThread(Thread):
#     def run(self):   #�̶��� -�����߳̿���ִ��֮�󣬱�ִ�еľ���run����
#         for i in range(1000):
#             print("���߳�",i)
#
#
# if __name__ == '__main__':
#     z=MyThread()
#     #z.run()#��ɷ������� -�����߳�
#     z.start()#�����߳�
#     for i in range(1000):
#         print("���߳�", i)
#     z.run()
#     pass



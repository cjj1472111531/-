# coding=gbk
# @file:03-Э��.py
# @data:2021/8/8 15:56
# Editor:clown
import time


# def dunc():
#     print("���� ·")
#     time.sleep(3)  # ��ǰ�̴߳�������״̬��cpu�ǲ�Ϊ���ҹ���
#     print("��������")


# if __name__ == "__main__":
#     dunc()

# input���� �����������״̬
# requests.get(��վ)  #���� ���������󷵻�����֮ǰ������Ҳ��������״̬
# һ������£��ڳ�����IO������ʱ�� �߳�һ�㴦������״̬

# Э�̣�����������IO������ʱ�򣬿���ѡ�����л�������������
# ����϶������һ��ִ��
# ��ʵ���ǿ��Կ����������첽����
import asyncio
import  time
# async def func():
#     print("������")
#
# if __name__ == "__main__":
#     g=func()  #��ʱ�������첽Э�̺�������ʱ����ִ�е���һ��Э�̶���
#     print(g)  #��ӡ��������ַ
#     asyncio.run(g)  #Э�̳���������Ҫasyncioģ���֧��


# async def fun1():
#     print("������")
# #  time.sleep(3) #�����������ͬ��������ʱ���첽���ж��� requests.get()Ҳ������
#     await asyncio.sleep(1) #�첽�����Ĵ���  #await�ǹ������˼
#     print("���")
#
# async def fun2():
#     print("one")
#     # time.sleep(3)
#     await asyncio.sleep(2)
#     print("one")
#
# async def fun3():
#     print("two")
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("two")
#
# async def fun4():
#     print("fivw")
#     # time.sleep(3)
#     await asyncio.sleep(8)
#     print("fivw")


# if __name__ == "__main__":
#     g=fun1()  #��ʱ�������첽Э�̺�������ʱ����ִ�е���һ��Э�̶���
#     f1=fun1()
#     f2=fun2()
#     f3=fun3()
#     f4=fun4()
#     takes=[f1,f2,f3,f4] #һ��������������� (Э��)
#     t1=time.time()
#     #�б�run �ǲ�ͬ��
#     asyncio.run(asyncio.wait(takes))  #Э�̳���������Ҫasyncioģ���֧��
#     t2=time.time()
#     print(t2-t1)


# async def fun1():
#     print("������")
# #  time.sleep(3) #�����������ͬ��������ʱ���첽���ж��� requests.get()Ҳ������
#     await asyncio.sleep(1) #�첽�����Ĵ���  #await�ǹ������˼
#     print("���")
#
# async def fun2():
#     print("one")
#     # time.sleep(3)
#     await asyncio.sleep(2)
#     print("one")
#
# async def fun3():
#     print("two")
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("two")
#
# async def fun4():
#     print("fivw")
#     # time.sleep(3)
#     await asyncio.sleep(5)
#     print("fivw")
#
# async def main():
#     # ��һ��д��
#     # f1=fun1()
#     # await f1 #һ��await��������������Э�̶���ǰ��
#     #�ڶ���д��
#     takes=[fun1(),fun2(),fun3(),fun4()]
#     await asyncio.wait(takes)
#
#
# if __name__ == "__main__":
#     g=fun1()  #��ʱ�������첽Э�̺�������ʱ����ִ�е���һ��Э�̶���
#     t1=time.time()
#     cgazhi=asyncio.run(main())
#     t2=time.time()
#     print(t2-t1)



# #�����������Ӧ��
# async def download(url):
#     print("��ʼ׼������")
#     await asyncio.sleep(2)#���������� requests.get ���ܷ�����
#     print("�������")
#
# async def main():
#     urls=[
#                 "http://www.baidu.com",
#                 "http://www.bilibili.com",
#                 "http://www.163.com"
#     ]
#     tasks=[]
#     for url in urls:
#         d=download(url)
#         tasks.append(d)
#     await asyncio.wait(tasks)
#
#
# if __name__=='__main__':
#     asyncio.run(main())

async def fun1():
    print("������")
#  time.sleep(3) #�����������ͬ��������ʱ���첽���ж��� requests.get()Ҳ������
    await asyncio.sleep(1) #�첽�����Ĵ���  #await�ǹ������˼
    print("���")

async def fun2():
    print("one")
    # time.sleep(3)
    await asyncio.sleep(2)
    print("one")

async def fun3():
    print("two")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("two")

async def main():
    tasks=[asyncio.create_task(fun1()), #py3.8�Ժ����asyncio.create_task()�Ͳ����о�����
           asyncio.create_task(fun2()), #����������Ϊһ��task
           asyncio.create_task(fun3())]
    await asyncio.wait(tasks)


if __name__=='__main__':
    t1=time.time()
    asyncio.run(main())
    t2=time.time()
    print(t2-t1)



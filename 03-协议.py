# coding=gbk
# @file:03-协议.py
# @data:2021/8/8 15:56
# Editor:clown
import time


# def dunc():
#     print("我跑 路")
#     time.sleep(3)  # 当前线程处于阻塞状态，cpu是不为问我工作
#     print("我跑完了")


# if __name__ == "__main__":
#     dunc()

# input（） 程序进行阻塞状态
# requests.get(网站)  #阻塞 在网络请求返回数据之前，程序也处于阻塞状态
# 一般情况下，在程序处于IO操作的时候 线程一般处于阻塞状态

# 协程：当程序遇见IO操作的时候，可以选择性切换到其他任务上
# 宏观上多个任务一起执行
# 其实我们可以看到多任务异步操作
import asyncio
import  time
# async def func():
#     print("啦啦啦")
#
# if __name__ == "__main__":
#     g=func()  #此时函数是异步协程函数，此时函数执行的是一个协程对象
#     print(g)  #打印的容器地址
#     asyncio.run(g)  #协程程序运行需要asyncio模块的支持


# async def fun1():
#     print("啦啦啦")
# #  time.sleep(3) #当程序出现了同步操作的时候，异步就中断了 requests.get()也会阻塞
#     await asyncio.sleep(1) #异步操作的代码  #await是挂起的意思
#     print("嘟嘟嘟")
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
#     g=fun1()  #此时函数是异步协程函数，此时函数执行的是一个协程对象
#     f1=fun1()
#     f2=fun2()
#     f3=fun3()
#     f4=fun4()
#     takes=[f1,f2,f3,f4] #一次性启动多个任务 (协程)
#     t1=time.time()
#     #列表run 是不同的
#     asyncio.run(asyncio.wait(takes))  #协程程序运行需要asyncio模块的支持
#     t2=time.time()
#     print(t2-t1)


# async def fun1():
#     print("啦啦啦")
# #  time.sleep(3) #当程序出现了同步操作的时候，异步就中断了 requests.get()也会阻塞
#     await asyncio.sleep(1) #异步操作的代码  #await是挂起的意思
#     print("嘟嘟嘟")
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
#     # 第一种写法
#     # f1=fun1()
#     # await f1 #一般await挂起来操作放在协程对象前面
#     #第二种写法
#     takes=[fun1(),fun2(),fun3(),fun4()]
#     await asyncio.wait(takes)
#
#
# if __name__ == "__main__":
#     g=fun1()  #此时函数是异步协程函数，此时函数执行的是一个协程对象
#     t1=time.time()
#     cgazhi=asyncio.run(main())
#     t2=time.time()
#     print(t2-t1)



# #在爬虫领域的应用
# async def download(url):
#     print("开始准备下载")
#     await asyncio.sleep(2)#是网络请求 requests.get 不能放这里
#     print("下载完成")
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
    print("啦啦啦")
#  time.sleep(3) #当程序出现了同步操作的时候，异步就中断了 requests.get()也会阻塞
    await asyncio.sleep(1) #异步操作的代码  #await是挂起的意思
    print("嘟嘟嘟")

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
    tasks=[asyncio.create_task(fun1()), #py3.8以后加上asyncio.create_task()就不会有警告了
           asyncio.create_task(fun2()), #把他帮他作为一个task
           asyncio.create_task(fun3())]
    await asyncio.wait(tasks)


if __name__=='__main__':
    t1=time.time()
    asyncio.run(main())
    t2=time.time()
    print(t2-t1)



# coding=gbk
# @file:04-aiohttp.py
# @data:2021/8/9 8:45
# Editor:clown
# requests.get() 同步代码，异步操作
import asyncio
import aiohttp

urls=[
"https://www.xxfoo.com/images/2021/06/12/20180916203725_31777d6b05343fc3c89e8.jpg",
"https://www.xxfoo.com/images/2021/06/05/3yuwiylwuuoh020350.jpg",
"https://www.xxfoo.com/images/2021/06/05/6b4usyjfzped020350.jpg"
]
async def aiodownload(url):
    #加上with之后他会自动帮你关闭文件
    # img_name=url.split("/")[-1]#切割1次取第一个 自己写的
    img_name=url.rsplit("/",1)[-1]#切割1次取第一个 自己写的
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #请求有了写入文件
            with open(img_name,mode="wb") as f:
                f.write(await resp.content.read()) #读取内容是异步，异步需要挂起
    print(img_name,"over")
            # resp.content.read() #==>等价于resp.content
            # resp.text()  #等价于 resp.text  json  没变
        # session.get()
        # session.post()
    # 发送请求 得到图片内容 保存到文件
    # aiohttp.ClientSession() #<==>requests模块
    # request.get() .post()
    #   session.get()  session.post

async def main():
    takes=[] #任务栏
    for url in urls:
        takes.append(aiodownload(url))

    await asyncio.wait(takes)

if __name__=="__main__":
    loop=asyncio.get_event_loop()  #解决loop问题
    loop.run_until_complete(main())
    # asyncio.run(main())




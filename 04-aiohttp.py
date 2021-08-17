# coding=gbk
# @file:04-aiohttp.py
# @data:2021/8/9 8:45
# Editor:clown
# requests.get() ͬ�����룬�첽����
import asyncio
import aiohttp

urls=[
"https://www.xxfoo.com/images/2021/06/12/20180916203725_31777d6b05343fc3c89e8.jpg",
"https://www.xxfoo.com/images/2021/06/05/3yuwiylwuuoh020350.jpg",
"https://www.xxfoo.com/images/2021/06/05/6b4usyjfzped020350.jpg"
]
async def aiodownload(url):
    #����with֮�������Զ�����ر��ļ�
    # img_name=url.split("/")[-1]#�и�1��ȡ��һ�� �Լ�д��
    img_name=url.rsplit("/",1)[-1]#�и�1��ȡ��һ�� �Լ�д��
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #��������д���ļ�
            with open(img_name,mode="wb") as f:
                f.write(await resp.content.read()) #��ȡ�������첽���첽��Ҫ����
    print(img_name,"over")
            # resp.content.read() #==>�ȼ���resp.content
            # resp.text()  #�ȼ��� resp.text  json  û��
        # session.get()
        # session.post()
    # �������� �õ�ͼƬ���� ���浽�ļ�
    # aiohttp.ClientSession() #<==>requestsģ��
    # request.get() .post()
    #   session.get()  session.post

async def main():
    takes=[] #������
    for url in urls:
        takes.append(aiodownload(url))

    await asyncio.wait(takes)

if __name__=="__main__":
    loop=asyncio.get_event_loop()  #���loop����
    loop.run_until_complete(main())
    # asyncio.run(main())




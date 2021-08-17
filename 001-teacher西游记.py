# coding=gbk
# @file:001-teacher西游记.py
# @data:2021/8/9 15:57
# Editor:clown
#%22 是双引号的意思
# http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
'''所有章节的名字'''
# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}

'''
头八章
http://dushu.baidu.com/api/pc/getDetail?data={%22book_id%22:%224306063500%22}
'''

'''
每一章内容的网站
http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}
'''
import aiofiles
import json
import requests
import asyncio
import aiohttp
chapter_url="http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}"
new_zhangurl="http://dushu.baidu.com/api/pc/getDetail?data={%22book_id%22:%224306063500%22}"
content_url="http://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|11348571%22,%22need_bookinfo%22:1}"
head={
"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/91.0.4472.124Safari/537.36"
,"Referer":"http://dushu.baidu.com/pc/detail?gid=4306063500"
    #防盗链
}
'''前八章的章节内容信息爬取'''
# dudu=requests.get(new_zhangurl,headers=head)
# # print(dudu.json())
# dudu=dudu.json()
# ghost=dudu["data"]["novel"]["firstEightList"]["first_chapter"]
# # print(ghost)
# for i in ghost:
#     print(i["title"],end="--")
#     print(i["cid"])


# resp=requests.get(chapter_url,headers=head)
# print(resp.json())

# resp=requests.get(content_url,headers=head)
# # print(resp.json())
# clown=resp.json()['data']["novel"]['content'] #单纯从页面上拿到小说内容
# print(clown)

'''
1.同步操作访问getCatalog 拿到所有章节的cid和名称
2.异步操作：访问getchaptercontent 下载所有文章的内容
'''
async def aiodwonload(cid,bood_id,title):
    data={
        "book_id": bood_id,
        "cid": f"{bood_id}|{cid}",
        "need_bookinfo": 1
    }
    #因为是json字符串 所以要引进json
    data=json.dumps(data) #变成一个字符串
    url=f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    #异步操作下载了呀
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resq:
            dic=await resq.json() #都需要挂起  只要能挂起就挂起
            # lala=dic['data']["novel"]['content']
            #之后写入文件
            async with aiofiles.open(title,mode="w",encoding="utf8") as f:
                await   f.write(dic['data']["novel"]['content']) #把内容写入



async def getCatelog(url):
    resp=requests.get(url,headers=head)
    # print(resp.json())
    dic=resp.json()["data"]["novel"]['items']
    tasks=[]
    for i in dic: #对应每一个章节名字和cid
        title=i['title']
        cid=i['cid']
        #准备异步任务
        tasks.append(aiodwonload(cid,book_id,title))
    await asyncio.wait(tasks)



if __name__=="__main__":
    book_id="4306063500"
    #把他这样必须要转义呀
    tou_url='http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' +book_id+ '"}'
    # getCatelog(tou_url) #因为是异步所以必须换种操作 async
    asyncio.run(getCatelog(tou_url))



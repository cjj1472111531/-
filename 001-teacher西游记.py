# coding=gbk
# @file:001-teacher���μ�.py
# @data:2021/8/9 15:57
# Editor:clown
#%22 ��˫���ŵ���˼
# http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
'''�����½ڵ�����'''
# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}

'''
ͷ����
http://dushu.baidu.com/api/pc/getDetail?data={%22book_id%22:%224306063500%22}
'''

'''
ÿһ�����ݵ���վ
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
    #������
}
'''ǰ���µ��½�������Ϣ��ȡ'''
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
# clown=resp.json()['data']["novel"]['content'] #������ҳ�����õ�С˵����
# print(clown)

'''
1.ͬ����������getCatalog �õ������½ڵ�cid������
2.�첽����������getchaptercontent �����������µ�����
'''
async def aiodwonload(cid,bood_id,title):
    data={
        "book_id": bood_id,
        "cid": f"{bood_id}|{cid}",
        "need_bookinfo": 1
    }
    #��Ϊ��json�ַ��� ����Ҫ����json
    data=json.dumps(data) #���һ���ַ���
    url=f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    #�첽����������ѽ
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resq:
            dic=await resq.json() #����Ҫ����  ֻҪ�ܹ���͹���
            # lala=dic['data']["novel"]['content']
            #֮��д���ļ�
            async with aiofiles.open(title,mode="w",encoding="utf8") as f:
                await   f.write(dic['data']["novel"]['content']) #������д��



async def getCatelog(url):
    resp=requests.get(url,headers=head)
    # print(resp.json())
    dic=resp.json()["data"]["novel"]['items']
    tasks=[]
    for i in dic: #��Ӧÿһ���½����ֺ�cid
        title=i['title']
        cid=i['cid']
        #׼���첽����
        tasks.append(aiodwonload(cid,book_id,title))
    await asyncio.wait(tasks)



if __name__=="__main__":
    book_id="4306063500"
    #������������Ҫת��ѽ
    tou_url='http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' +book_id+ '"}'
    # getCatelog(tou_url) #��Ϊ���첽���Ա��뻻�ֲ��� async
    asyncio.run(getCatelog(tou_url))



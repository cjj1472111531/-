# coding=gbk
# @file:000_Э�̰ǹ����μ�.py
# @data:2021/8/9 10:56
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
import json
import requests
import asyncio
import aiohttp
chapter_url="http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22"
new_zhangurl="http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}"
content_url="http://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|11348571%22,%22need_bookinfo%22:1}"
head={
"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/91.0.4472.124Safari/537.36"
,"Referer":"http://dushu.baidu.com/pc/detail?gid=4306063500"
    #������
}
#ͬ��ȥ��
def download(cid,book_id,title):
    data={
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data=json.dumps(data)
    # print(data)
    son_url=f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    resp=requests.get(son_url,headers=head)
    dist=resp.json()
    # print(dist)
    with open(title,mode="w",encoding="utf8") as f:
        f.write(dist['data']["novel"]['content'])


'''ǰ���µ��½�������Ϣ��ȡ'''
bood_id="4306063500"
dudu=requests.get(new_zhangurl,headers=head)
# print(dudu.json())
dudu=dudu.json()
ghost=dudu["data"]["novel"]['items']
# print(ghost)
for i in ghost:
    # print(i["title"],end="--")
    # print(i["cid"])
    title = i['title']
    cid = i['cid']
    download(cid,bood_id,title)

# resp=requests.get(chapter_url,headers=head)
# print(resp.json())

# resp=requests.get(content_url,headers=head)
# # print(resp.json())
# clown=resp.json()['data']["novel"]['content'] #������ҳ�����õ�С˵����
# print(clown)


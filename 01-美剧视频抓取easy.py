# coding=gbk
# @file:01-美剧视频抓取easy.py
# @data:2021/8/10 10:01
# Editor:clown
import requests
import re
# msu8_url="https://vod.bunediy.com/20210621/dx9xCgdj/index.m3u8"
from bs4 import BeautifulSoup


'''
流程：
    1.拿到视频源代码
    2.从源代码中提取m3u8的url
    3. 下载没u8
    4.读取m3u8文件，下载视频
    5.合并视频
'''

# 获取m3u8的地址
url="https://www.91mjw.cc/video/2868-0-0.html"
head={
"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/91.0.4472.124Safari/537.36"
}
resp=requests.get(url,headers=head)
# print(resp.text)
obj=re.compile(r'var next="(?P<m3u8_url>.*?)";var prePage=',re.S) #re正则
# resp=str(resp.text)
dudu=obj.search(resp.text)
# print(dudu.group('m3u8_url'))
m3u8_url=dudu.group('m3u8_url')
resp.close()
#下载m3u8文件
resp2=requests.get(m3u8_url,headers=head)
# 二进制写进去
with open("瑞克和莫蒂.m3u8",mode='wb') as f:
    f.write(resp2.content)
resp2.close()
print("over")





'''re,bs4结合使用试试'''
# clown=BeautifulSoup(resp,"html.parser")
# zz=clown.find("div",class_="box")
# print(zz)
# zz=str(zz)
# lala=obj.search(zz)
# # print(lala.group('m3u8_url'))
# msu8_url=lala.group('m3u8_url')






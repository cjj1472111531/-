# coding=gbk
# @file:01-������Ƶץȡeasy.py
# @data:2021/8/10 10:01
# Editor:clown
import requests
import re
# msu8_url="https://vod.bunediy.com/20210621/dx9xCgdj/index.m3u8"
from bs4 import BeautifulSoup


'''
���̣�
    1.�õ���ƵԴ����
    2.��Դ��������ȡm3u8��url
    3. ����ûu8
    4.��ȡm3u8�ļ���������Ƶ
    5.�ϲ���Ƶ
'''

# ��ȡm3u8�ĵ�ַ
url="https://www.91mjw.cc/video/2868-0-0.html"
head={
"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/91.0.4472.124Safari/537.36"
}
resp=requests.get(url,headers=head)
# print(resp.text)
obj=re.compile(r'var next="(?P<m3u8_url>.*?)";var prePage=',re.S) #re����
# resp=str(resp.text)
dudu=obj.search(resp.text)
# print(dudu.group('m3u8_url'))
m3u8_url=dudu.group('m3u8_url')
resp.close()
#����m3u8�ļ�
resp2=requests.get(m3u8_url,headers=head)
# ������д��ȥ
with open("��˺�Ī��.m3u8",mode='wb') as f:
    f.write(resp2.content)
resp2.close()
print("over")





'''re,bs4���ʹ������'''
# clown=BeautifulSoup(resp,"html.parser")
# zz=clown.find("div",class_="box")
# print(zz)
# zz=str(zz)
# lala=obj.search(zz)
# # print(lala.group('m3u8_url'))
# msu8_url=lala.group('m3u8_url')






# coding=gbk
# @file:011-瑞克和莫蒂视频下载.py
# @data:2021/8/10 16:03
# Editor:clown
'''
4.读取m3u8文件，下载视频
5.合并视频
'''
import os

# print(os.getcwd())#当前目录
# print(os.path.dirname(os.getcwd()))#上一级的目录
import requests
n=1
with open('瑞克和莫蒂.m3u8',mode="r",encoding="utf-8") as f:
    for line in f: #读一行代码
        line=line.strip()#先去掉空格，换行符，空白
        if line.startswith("#"): #匹配开头符号
            continue
        else:
            # print(line)
            resp=requests.get(line)
            f=open(f"video/{n}.ts",mode="wb")#写入特定的位置
            f.write(resp.content)
            f.close()
            resp.close()
            n+=1
            print("完成了一个")
# 5.合并视频

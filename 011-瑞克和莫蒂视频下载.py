# coding=gbk
# @file:011-��˺�Ī����Ƶ����.py
# @data:2021/8/10 16:03
# Editor:clown
'''
4.��ȡm3u8�ļ���������Ƶ
5.�ϲ���Ƶ
'''
import os

# print(os.getcwd())#��ǰĿ¼
# print(os.path.dirname(os.getcwd()))#��һ����Ŀ¼
import requests
n=1
with open('��˺�Ī��.m3u8',mode="r",encoding="utf-8") as f:
    for line in f: #��һ�д���
        line=line.strip()#��ȥ���ո񣬻��з����հ�
        if line.startswith("#"): #ƥ�俪ͷ����
            continue
        else:
            # print(line)
            resp=requests.get(line)
            f=open(f"video/{n}.ts",mode="wb")#д���ض���λ��
            f.write(resp.content)
            f.close()
            resp.close()
            n+=1
            print("�����һ��")
# 5.�ϲ���Ƶ

# coding=gbk
# @file:01-selenium��̽.py
# @data:2021/8/10 19:47
# Editor:clown
# �ܲ����ó�������������������������ɸ��ָ��ӵĲ����������������յĽ��
# seleniumģ��  ���Զ������Թ���
#  ������� ����һ��ȥ���������
# ����Ա���Դ�selenium��ֱ����ȡ��ҳ�ϵĸ�����Ϣ
# �������
# ��װ selenium
# ������������� �ѽ�ѹ����������� chromedriver ����python��������
# ��selenium�����ȸ������
from  selenium.webdriver import Chrome #��˭������͵���ɶ

#���������Ŀ��
web=Chrome()
#��һ����վ
web.get("https://www.baidu.com/")
print(web.title)
# web.close()









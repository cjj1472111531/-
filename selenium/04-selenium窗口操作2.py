# coding=gbk
# @file:04-selenium���ڲ���2.py
# @data:2021/8/11 10:47
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
# ���ҳ�������� iframe������ô����
web.get("https://www.91mjw.cc/video/2868-0-0.html")

# swith_toת���ӽ�
# ����iframe�Ļ�������Ҫ���õ�iframe��Ȼ���л��ӽǵ�iframe����Ȼ��ſ����õ�����
iframe = web.find_element_by_xpath('//*[@id="player"]/iframe')
web.switch_to.frame(iframe)
# web.switch_to.default_content()#�л���Ĭ�ϵĴ��� ����һ��ʼ�򿪵Ĵ��� #�л���

tect = web.find_element_by_xpath('//*[@id="dplayer"]/div[6]/div[2]/a').text
print(tect)

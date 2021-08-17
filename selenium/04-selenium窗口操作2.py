# coding=gbk
# @file:04-selenium窗口操作2.py
# @data:2021/8/11 10:47
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
# 如果页面中遇到 iframe问题怎么处理
web.get("https://www.91mjw.cc/video/2868-0-0.html")

# swith_to转换视角
# 处理iframe的话，必须要先拿到iframe，然后切换视角到iframe，再然后才可以拿到数据
iframe = web.find_element_by_xpath('//*[@id="player"]/iframe')
web.switch_to.frame(iframe)
# web.switch_to.default_content()#切换到默认的窗口 就是一开始打开的窗口 #切回来

tect = web.find_element_by_xpath('//*[@id="dplayer"]/div[6]/div[2]/a').text
print(tect)

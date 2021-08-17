# coding=gbk
# @file:06-西游记展开.py
# @data:2021/8/11 12:24
# Editor:clown
from selenium.webdriver import Chrome
web=Chrome()
web.get('http://dushu.baidu.com/pc/detail?gid=4306063500')
web.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[2]/button').click()





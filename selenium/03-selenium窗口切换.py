# coding=gbk
# @file:03-selenium窗口切换.py
# @data:2021/8/11 9:41
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
web=Chrome()
web.get("http://lagou.com")
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
work=web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(2)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[3]/div[1]/div[1]/div[1]/a/h3').click()

#如何进入新窗口中进行提取
# 在selenium眼中，新窗口是不切过来的
web.switch_to.window(web.window_handles[-1])#这个函数就是在转换到信界面 最后一个
#在新窗口中提取内容

job_info=web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_info)
print("-"*30)
#是关掉最新打开的子窗口
web.close()
#变更selenium视角 从新打开的窗口变回之前的
web.switch_to.window(web.window_handles[0])
#测试看能不能拿到主页面h3里面的内容
# //*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3
# //*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a').text,end="--")
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)




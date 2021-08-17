# coding=gbk
# @file:02-selenium各种操作.py
# @data:2021/8/10 20:52
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get("http://www.lagou.com/")

# 找到某个元素 点击他 xpath
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# elements 是找一堆
el.click()  # 点击事件

# ghost = input("请输入你想查询的职业:")
# 找到输入框  输入相关信息 进行查找 回车是ENDER
work = web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)

# 找到搜索 输入相关信息 # //*[@id="search_button"] ==》输入回车/或者点击搜索按钮
time.sleep(1)
# 查找数据存放的位置，进行数据提取
# 找到页面中存放数据所有的li 因为找的是一堆
li_list=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name=li.find_element_by_tag_name("h3").text #h3就是用by_tag_name 标签？
    salary=li.find_element_by_xpath('./div/div/div[2]/div/span').text
    jingyan=li.find_element_by_xpath('./div[1]/div[1]/div[2]/div').text
    cname=li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    number=li.find_element_by_xpath('./div[1]/div[2]/div[2]').text
    info=li.find_element_by_xpath('./div[2]/div[2]').text
    print(cname,end="--")
    print(job_name,end="--")
    print(salary,end="--")
    print(jingyan,end="--")
    print(number,end="--")
    print(info)








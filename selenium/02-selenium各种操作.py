# coding=gbk
# @file:02-selenium���ֲ���.py
# @data:2021/8/10 20:52
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get("http://www.lagou.com/")

# �ҵ�ĳ��Ԫ�� ����� xpath
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# elements ����һ��
el.click()  # ����¼�

# ghost = input("�����������ѯ��ְҵ:")
# �ҵ������  ���������Ϣ ���в��� �س���ENDER
work = web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)

# �ҵ����� ���������Ϣ # //*[@id="search_button"] ==������س�/���ߵ��������ť
time.sleep(1)
# �������ݴ�ŵ�λ�ã�����������ȡ
# �ҵ�ҳ���д���������е�li ��Ϊ�ҵ���һ��
li_list=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name=li.find_element_by_tag_name("h3").text #h3������by_tag_name ��ǩ��
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








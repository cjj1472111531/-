# coding=gbk
# @file:03-selenium�����л�.py
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

#��ν����´����н�����ȡ
# ��selenium���У��´����ǲ��й�����
web.switch_to.window(web.window_handles[-1])#�������������ת�����Ž��� ���һ��
#���´�������ȡ����

job_info=web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_info)
print("-"*30)
#�ǹص����´򿪵��Ӵ���
web.close()
#���selenium�ӽ� ���´򿪵Ĵ��ڱ��֮ǰ��
web.switch_to.window(web.window_handles[0])
#���Կ��ܲ����õ���ҳ��h3���������
# //*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3
# //*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a').text,end="--")
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)




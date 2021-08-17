# coding=gbk
# @file:05-��ͷ�����.py
# @data:2021/8/11 11:23
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select  # ����������İ�
from selenium.webdriver.chrome.options import Options
import time

#׼���ò������ã�
opt=Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt) #�Ѳ�������ֵ���õ�������� ��ͷ���������

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
# �����б�  select ��λ�����б�
sel_el= web.find_element_by_xpath('//*[@id="OptionDate"]')
# xpath�õ��Ķ������ǽڵ�element
# ��Ԫ�ؽ��а�װ����װ�������˵�
sel=Select(sel_el)
#���������������λ��
for i in range(len(sel.options)): #i ����ÿһ�������������λ��
    sel.select_by_index(i)#�������������л�
    # sel.select_by_value()#����ֵ�����л�
    # sel.select_by_visible_text()#���������ı������л�
    time.sleep(2)
    #ֱ�Ӱ�������������� ţ��
    table=web.find_element_by_xpath('//*[@id="TableList"]/table')
    print(table.text) #��ӡ�����ı���Ϣ
    print("==============================================")
    break
print("�������")
web.close()

time.sleep(2)
#����õ�ҳ�����F12 ��Elements���������ݼ����Լ�jsִ��֮��Ľ����html���ݣ�
print(web.page_source) #ֱ�ӿ��Դ�f12������


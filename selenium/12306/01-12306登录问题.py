# coding=gbk
# @file:01-12306��¼����.py
# @data:2021/8/11 17:22
# Editor:clown
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
#�����ĳ���ʶ���� ��ô��
# chrome�汾�� С��88
'''
ȥ�Զ�������� ȥ console�� Ѱ��window.navigator.webdriver ��false ���� true 
�������������ʱ��(��ʱû�м����κ���ҳ����)����ҳ��Ƕ��js���� ȥ��webdriver
'''
# web = Chrome()
#
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#    navigator.webdriver = undefined
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })
# web.get(xxxxxxx)
#�汾�Ŵ���88
opt=Options()
opt.add_argument('--disable-blink-features=AutomationControlled')


#��ʼ������ӥ
chaojiying = Chaojiying_Client('1472111531', 'qq1472111531', '920945')
# opt=Options()
# opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')

web=Chrome(options=opt)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(2)
name='15574426396'
password='qq1472111531'
#�ȴ�����֤��
veryify_img_ele=web.find_element_by_xpath('//*[@id="J-loginImg"]')

#�ó���ӥȥʶ��
dic=chaojiying.PostPic(veryify_img_ele.screenshot_as_png,9004) #9004����λ�� x1,y1|x2,y2
result=dic['pic_str']
print(result)
#���ַ���������
rs_list=result.split("|")  #�и�֮�� ֱ�ӱ���б�
# print(rs_list)
for rs in rs_list:
    # print(rs)
    x_y=rs.split(",")  #�ж���
    x=int(x_y[0])   #��Ϊ�õ��Ķ����ַ��� ����������
    y=int(x_y[1])
    print(x,"---",y)
    # ������ƶ���ĳһ��λ�ã�Ȼ����
    # ����-���ƿ�����-��������-����Ь��-�����·�    -����ʼִ�����Ĳ���
    # �ƶ��ڵ� ����ƫ������һ����� ��ͼƬ����ƫ���� �ٽ��е��
    # ��һ������ �ǻ���  �ڶ����� xƫ�Ƶ��� �������� yƫ�Ƶ��� perform ����
    ActionChains(web).move_to_element_with_offset(veryify_img_ele,x,y).click().perform()

#���������¼
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(1)

#�����û���������
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("15574426396")
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('qq1472111531')

time.sleep(1)
#���������¼
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)  #��ʱ���в�ͨ������
# ��ק //*[@id="nc_1__scale_text"]/span
but=web.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
ActionChains(web).drag_and_drop_by_offset(but,300,0).perform()
web.find_element_by_xpath('//*[@id="pop_162918847086318790"]/div[2]/div[3]/a').click()




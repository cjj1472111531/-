# coding=gbk
# @file:08-����ӥ�ɳ���ӥ.py
# @data:2021/8/11 16:38
# Editor:clown
from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
web=Chrome()
web.get('http://www.chaojiying.com/user/login')
data={
}

#������֤��  screenshot_as_png��ȡ��Ļ��Ϣ֮�����ó�png��ʽ
img=web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('1472111531', 'qq1472111531', '920945')
# im = open(img, 'rb').read()  # ͼƬ�����ֽ� (�ֽ�)
# 1902 ��֤������  �ٷ���վ>>�۸���ϵ 3.4+�� print ��Ҫ��()
dic=chaojiying.PostPic(img, 1004)
code_verify=dic['pic_str']

name='1472111531'
password='qq1472111531'
#��ҳ���������û��������룬��֤��
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(name)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code_verify)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()


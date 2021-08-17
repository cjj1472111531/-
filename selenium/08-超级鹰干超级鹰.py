# coding=gbk
# @file:08-超级鹰干超级鹰.py
# @data:2021/8/11 16:38
# Editor:clown
from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
web=Chrome()
web.get('http://www.chaojiying.com/user/login')
data={
}

#处理验证码  screenshot_as_png截取屏幕信息之后设置成png格式
img=web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('1472111531', 'qq1472111531', '920945')
# im = open(img, 'rb').read()  # 图片所有字节 (字节)
# 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
dic=chaojiying.PostPic(img, 1004)
code_verify=dic['pic_str']

name='1472111531'
password='qq1472111531'
#想页面中填入用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(name)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code_verify)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()


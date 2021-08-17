# coding=gbk
# @file:01-12306登录问题.py
# @data:2021/8/11 17:22
# Editor:clown
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
#如果你的程序被识别了 怎么办
# chrome版本号 小于88
'''
去自动化浏览器 去 console中 寻找window.navigator.webdriver 看false 还是 true 
在启动浏览器的时候(此时没有加载任何网页内容)，向页面嵌入js代码 去掉webdriver
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
#版本号大于88
opt=Options()
opt.add_argument('--disable-blink-features=AutomationControlled')


#初始化超级鹰
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
#先处理验证码
veryify_img_ele=web.find_element_by_xpath('//*[@id="J-loginImg"]')

#用超级鹰去识别
dic=chaojiying.PostPic(veryify_img_ele.screenshot_as_png,9004) #9004坐标位置 x1,y1|x2,y2
result=dic['pic_str']
print(result)
#对字符串做处理
rs_list=result.split("|")  #切割之后 直接变成列表
# print(rs_list)
for rs in rs_list:
    # print(rs)
    x_y=rs.split(",")  #切逗号
    x=int(x_y[0])   #因为拿到的都是字符串 而不是数字
    y=int(x_y[1])
    print(x,"---",y)
    # 让鼠标移动到某一个位置，然后点击
    # 醒啦-》掀开被子-》做起来-》穿鞋子-》穿衣服    -》开始执行最后的操作
    # 移动节点 带着偏移量的一个结点 从图片来做偏移量 再进行点击
    # 第一个参数 是基点  第二个是 x偏移的量 第三个是 y偏移的量 perform 运行
    ActionChains(web).move_to_element_with_offset(veryify_img_ele,x,y).click().perform()

#点击立即登录
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(1)

#输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("15574426396")
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('qq1472111531')

time.sleep(1)
#点击立即登录
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)  #有时候行不通就休眠
# 拖拽 //*[@id="nc_1__scale_text"]/span
but=web.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
ActionChains(web).drag_and_drop_by_offset(but,300,0).perform()
web.find_element_by_xpath('//*[@id="pop_162918847086318790"]/div[2]/div[3]/a').click()




# coding=gbk
# @file:05-无头浏览器.py
# @data:2021/8/11 11:23
# Editor:clown
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select  # 下拉框引入的包
from selenium.webdriver.chrome.options import Options
import time

#准备好参数配置：
opt=Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt) #把参数配置值设置到浏览器中 无头浏览器参数

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
# 下拉列表  select 定位下拉列表
sel_el= web.find_element_by_xpath('//*[@id="OptionDate"]')
# xpath拿到的东西都是节点element
# 对元素进行包装，包装成下拉菜单
sel=Select(sel_el)
#让浏览器调整它的位置
for i in range(len(sel.options)): #i 就是每一个下拉框的索引位置
    sel.select_by_index(i)#根据索引进行切换
    # sel.select_by_value()#根据值进行切换
    # sel.select_by_visible_text()#根据所见文本进行切换
    time.sleep(2)
    #直接把整个表给干下来 牛逼
    table=web.find_element_by_xpath('//*[@id="TableList"]/table')
    print(table.text) #打印所以文本信息
    print("==============================================")
    break
print("运行完毕")
web.close()

time.sleep(2)
#如何拿到页面代码F12 中Elements（经过数据加载以及js执行之后的结果的html内容）
print(web.page_source) #直接可以打开f12的内容


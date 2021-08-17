# coding=gbk
# @file:01-selenium初探.py
# @data:2021/8/10 19:47
# Editor:clown
# 能不能让程序连接浏览器，让浏览器来完成各种复杂的操作，我来接受最终的结果
# selenium模块  ：自动化测试工具
#  打开浏览器 像人一样去操作浏览器
# 程序员可以从selenium中直接提取网页上的各种信息
# 环境搭建：
# 安装 selenium
# 下载浏览器驱动 把解压的浏览器躯体 chromedriver 放在python解释器中
# 让selenium启动谷歌浏览器
from  selenium.webdriver import Chrome #是谁浏览器就导入啥

#创建浏览器目标
web=Chrome()
#打开一个网站
web.get("https://www.baidu.com/")
print(web.title)
# web.close()









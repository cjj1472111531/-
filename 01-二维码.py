# coding=gbk
# @file:01-二维码.py
# @data:2021/8/3 16:06
# Editor:clown
from MyQR import  myqr
# myqr.run(
#     words="https://www.baidu.com",
#     picture=(r"C:\\Users\\Administrator.DESKTOP-43F1443\\Desktop\\lala.png"),
#     colorized=True,
# )

myqr.run(
    words="https://www.baidu.com",
    picture=(r"C:\Users\Administrator.DESKTOP-43F1443\Desktop\thescond.gif"),
    colorized=True,
    version=5,
    level='H',
    contrast=1.0,
    save_name='eqeq.gif',
    brightness=1.0,
    save_dir=r'F:\\python_yanyanyanayan\\pythonProject_requestmodule_up'
)



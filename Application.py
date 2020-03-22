#ZZUjksb自动填写 Ver 1.8
ver = 1.8
#By DJK233
#By Clok Much
'''


1 准备使用
    1.1 下载安装 Mozilla Firefox
            请在此网站下载 Mozilla Firefox：
                https://www.firefox.com.cn/
            然后安装（安装步骤略）.
    
    1.2 将 Mozilla Firefox 所在目录添加到系统环境变量 PATH 中，
        安装目录一般为：
            C:\Program Files\Mozilla Firefox
        具体步骤略（以后的版本再加个 Word 文档详细说明吧 qwq）.

    1.3 使用 pip 安装 selenium 库，为提升安装体验，建议在 pip 
        所在目录执行如下安装命令（使用清华大学的源，安装比较快
         qwq）：
            pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
        具体步骤略（以后的版本再说吧 qwq）.

    1.5 至此，你已经可以运行 健康上报 了，后续将介绍如何配置 健康上报 .

2 配置 健康上报
    2.1 运行 Application.py ，按提示填写你的学号和密码.

    2.2（可选） 为 Application.py 创建快捷方式，以快速运行.


'''

#导入所需库与函数体
from time import sleep
from jksb import *
import selenium

#简述版本情况
print("jksb.Ver" + str(ver) + '\n')

#创建或读取配置文件
chk_config()

###以下为运行部分###
#检查今日是否已运行
run()
#没有上报时的流程
print("\n今天没有运行健康上报，正在准备上报...")
jksb()
creat_inct(get_name())
#说明
print("\n\n\n运行结束！您可以直接关闭本窗口.")
input()

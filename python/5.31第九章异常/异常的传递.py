#来一个异常
num=1
def x1():
    print("x1在执行")
    num=1/0  #肯定异常的语句
    print("x1执行结束")

def x2():
    print("x2开始执行")
    x1()
    print("x2结束执行")

def main():
    try:
        x2()
    except Exception as e:
        print("sb了吧")
main()

###############################自定义模块调用
from 自定义模块 import x1 as kk
i=kk()
print(f"{i}")
##########那如果是两个模块里面的两个同名函数呢?
# 调用时候后一个会把前一个覆盖掉
from 自定义模块 import *

"""
模块在使用前需要先导入 导入的语法如下:
[from 模块名]import[模块 | 类 | 变量 | 函数 |*][as 别名]

常用的组合形式如:
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import模块名as别名
from模块名import功能名as别名
"""
###使用import导入time模块使用sleep功能
import time  #内置的time.py文件
print("我爱你")
time.sleep(1)   #time里的sleep函数 相当于delay1秒
print("我也爱你")  #延迟了五秒钟出现这条

######使用form导入time模块的sleep函数
from time import sleep    #表示我只使用time里的sleep函数功能
print("真的吗")
sleep(1)     #因为只是导入了sleep函数,所以不需要在前面加time.
print("是的")
from time import * #这个的意思是time模块里的全部功能我都要
sleep(1)
print("谢谢你")
##########设置别名
import time as love
love.sleep(1)
print("哈哈")
#####也可以使用form设置别名
from time import sleep as ll  #这里sleep函数被设置别名为ll
ll(1)
print("哈哈哈")





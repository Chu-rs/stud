#字符串定义
num1='你好'
num2="你好"
num3="""你好"""
print(num1,num2,num3)
#用单引号去定义字符串，里面显示双引号
num4='"sb"'
print(num4)
#用双引号去显示单引号
num5="'dsb'"
print(num5)
#用\改变效用
num6="\"dsbb"
print(num6)

#字符串拼接
#变量也可以被拼接
yd="三块钱"
print("写光源"+yd+" 一斤")
print("写光源",yd,"一斤")

#字符串格式化            占位型拼接
yyds="有钱"
message="马云%s"%yyds
print(message)
#第一个百分号表示：我要占位了，第二个表示占位的是什么

#多个占位时
hero="卧槽"
vg=99
ksg="在王者荣耀联赛中%s，hero打赢了gk%s"%(hero,vg)
print(ksg)

#上面的%s是转成字符串的占位
#%d是转成整数型的占位
#%f是转成浮点型的占位

#但是有更优雅的方法：f"内容{变量}“
name="略略略"
print(f"我是{name}")


#格式化的精度控制
 #控制宽度和精度
 #使用m.n   如%7.2f   对11.345就变成了【】【】11.35  其小数点和小数部分也算宽度
num=11.145
print('在%5d情况下'%num)
print('在%7.2f情况下'%num)

#对表达式格式化   表达式：有具体结果的代码语句
print("1*1的结果是：%d"%(1*1))
print(f"1*1的结果是{1*1}")
print("我觉得你脾气：%s"%type('坏'))

#数据输入input函数
print("请输入密码：")
kk=input()
print("你的密码是：",kk)
print(f"你的密码是：{kk}")







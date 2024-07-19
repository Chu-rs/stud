"""
设计表格,打印表格,填写表格
设计类 class
创建对象
对象属性赋值


"""
import time


class Student:
    name=None
    gender=None
    nationality=None
    age=None
    #创建类的行为
    def y1(self):   #这个self必须有,但是不是形参,用来表达类对象自身的意思

        print(f"全民制作人们大家好,我是练习时长{self.age}的个人练习生{self.name},我来自{self.nationality}")
    def y2(self,k):
        print(f"我很喜欢你,{k}")
#创建可用对象
x1=Student()#这里x1即是对象也是变量

#对对象进行赋值
x1.name="蔡虚坤"
x1.gender="男"
x1.nationality="日本"
x1.age=2.5
print(x1.name)
print(x1.gender)
print(x1.nationality)
print(x1.age)

x1.y1()#调用类函数
x1.y2("???")
"""
python 是面向对象的编程

类的具体使用语法
class 类名字:
    类的属性:定义在类中的变量
    类的行为:定义在类里的函数
"""
#设计一个闹钟类
class clock:
    id = None
    price = None
    def ring(self):
        import winsound  #python内置响铃程序
        winsound.Beep(2000,3000)  #频率与时间
#构建闹钟对象使其干活
clock1=clock()
clock1.id=int(input(f"输入闹钟id号:"))
clock1.price=int(input(f"请输入价格:"))
print(f"闹钟id:{clock1.id},闹钟价格:{clock1.price}")
time.sleep(3)
clock1.ring()
#这种对象可以做出无数个









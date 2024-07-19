#以传参方式的
#以__init__()方法的
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





#以传参方式的
#以__init__()方法的
import time


class Student2:
    name=None
    gender=None
    nationality=None
    age=None
    #创建类的行为
    def __init__(self,name,gender,nationlity,age):
        self.name=name
        self.nationality=nationlity
        self.gender=gender                 #这四条又有赋值功能又有定义功能
        self.age=age
        print(f"全民制作人们大家好,我是练习时长{self.age}的个人练习生{self.name},我来自{self.nationality}")


Student2("蔡徐坤",2,"法国",2)




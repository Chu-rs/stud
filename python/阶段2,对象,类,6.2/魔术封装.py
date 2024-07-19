#内置的类方法
"""
__init__构造方法
__str__字符串方法
__lt__小于大于符号比较                    可以用到排序中
__le__小于等于,大于等于符号比较
__eq__   ==这个符号的比较


"""
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
        # print(f"全民制作人们大家好,我是练习时长{self.age}的个人练习生{self.name},我来自{self.nationality}")


    def __str__(self):#控制把我们的字符串变成对象
        return f"student类对象,name={self.name},age={self.age}"



    def __lt__(self, other):
        return self.age < other.age




    def __le__(self, other):
        return self.age <= other.age


    def __eq__(self, other):
        return self.age == other.age


stu1=Student2("蔡徐坤",2,"法国",2)
stu2=Student2("周杰伦",2,"中国" ,3)


print(stu1) #如果没有__str__,输出就是<__main__.Student2 object at 0x0000022588F19610>
print(stu1<stu2)#结果:true
print(stu1<=stu2)#结果true
print(stu1==stu2)#结果true


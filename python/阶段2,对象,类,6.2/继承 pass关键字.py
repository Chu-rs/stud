"""
苹果手机版本迭代
一个子类可以有多个父类
有多个继承

"""
class iphone5:
    IMEI=76125
    producer=None    #定义公开变量

    __vol=4.2  #定义私有变量     不能被类对象直接使用
    def kk(self):
        print(f"kk模式")
    def call_5G(self):
        if self.__vol>=5:
            print(f"当前电压:{self.__vol},5G可使用")
        else:
            self.kk()
            print("用个鸡巴毛用")

##########################以上是5的老版本
#再给一个父亲

class sb:
    def sb(self):
        print("确实挺sb的")


##########################以下是我们要做的苹果6

class iphone6(iphone5,sb):
#然后只需要写新功能就行了
#复写父类属性
    IMEI = 35
#复写父类方法:
    def call_5G(self):
        print("反正就是可以用")

#现在调用父类方法
    def gg(self):

        iphone5.call_5G(self)
    
"""
复写:对继承来的父类不满意,可以覆盖掉
调用父类成员:
"""
"""   
    def call_6g(self):
#私有变量好像继承不了

        if self.IMEI<=5:
            print(f",5G可使用")
        else:
            #但是私有函数也不行
            #公有函数可以
            self.sb()
            self.kk()
            print("用个鸡巴毛用")
"""




iphone=iphone6()
################如果爹里面的类的名字一样,那就继承左边的,谁先当爹谁就是大爹

iphone.gg()#意思就是说当调用父类时候,私有的就可以用了
####################那我复写以后我父类的我还想要怎么办
"""
方法1
使用成员变量:父类名.成员变量
成员方法:父类名.成员方法(self)
方法2
super().成员变量
super().成员方法()
"""















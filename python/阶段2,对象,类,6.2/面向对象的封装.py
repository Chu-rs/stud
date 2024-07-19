"""
面向对象有三个特性
封装
继承
多态

封装:将现实世界的事物描述为程序里的类
封装主要搞那些隐藏的行为和属性
类中提供了私有成员变量和私有成员方法  变量名或者方法名前面以__开头

"""
class iphone5:
    IMEI=76125
    producer=None    #定义公开变量

    __vol=4.2  #定义私有变量     不能被类对象直接使用
    def __kk(self):
        print(f"kk模式")
    def call_5G(self):
        if self.__vol>=5:
            print(f"当前电压:{self.__vol},5G可使用")
        else:
            self.__kk()
            print("用个鸡巴毛用")
#构建类对象
iphone1=iphone5()

#被类中其他成员使用
iphone1.call_5G()




















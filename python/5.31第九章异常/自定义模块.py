__all__=['x1']      #这个的意思是,假如有要全部调用自定义模块时候
#就算是全调用,也是调用[]里的函数,但是可以被手动导入
def x1():
    y=10
    x=int(input("输入一个数字"))
    k=x+y

    return k

def x2():
    y=10
    x=int(input("输入一个数字"))
    k=x+y

    return k
if __name__ == '__main__':#####意思是以下语句本文件运行时启动,但是调用时候不运行
    print("shh")
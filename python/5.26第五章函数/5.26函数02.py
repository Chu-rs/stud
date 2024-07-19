############函数传入数据
def cheng(i,j):
    kk=i*j
    return kk

a=int(input("请输入一个数"))
b=int(input("请再输入一个数"))
gg=cheng(a,b)

print(f"函数相乘的值：{gg}")
#################################
print()

#返回值定义语法
#在if判断中None相当于flase
#return None 相当于C语言里的return 0

##################函数的嵌套调用
#我要输入1个数字，假如说它大于5，
# 那么他乘以三然后减去2，如果小于那就直接输出。然后判断是否大于20
#如果是的，直接输出，如果不是，加上5输出

def num1(q):
    if q>20:
        return q
    else:
        q+=5
        return q

def num2(m):
    if m<5:
        return m
    else:
        m=(m*3)-2
        ts=num1(m)
        return ts
T=int(input("请大哥输入一个数"))
G=num2(T)
print(G)
"""
局部变量与全局变量
就像上面的ts，就是局部变量，ts并不能在函数外被拿出来输出或者使用
"""





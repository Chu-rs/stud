"""
做一个ATM，然后
输入1查询余额，输入2存款
输入3取款
输入4退出
"""
import random
num=random.randint(10000,10000000)
def shuru1(a):
    print(f"您的余额为{num}")
def shuru2(b):
    b=int(input("请问您存款数："))
    return b
def shuru3(c):
    c=int(input("请输入您的取款数："))
    return c
def shuru4():
    print("好的，再见")

    print("欢迎使用本ATM，请问有什么可以帮到您？")
    print("输入1查询余额\t\t输入2进行存款")
    print("输入3进行取款\t\t输入4退出")
    print()


m=int(input())





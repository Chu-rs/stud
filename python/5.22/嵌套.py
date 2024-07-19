#满足前置条件后的二次判断需求
age=int(input("你的岁数是："))
if age>=18:
    print("那赶紧谈个恋爱吧")

    if str(input("谈恋爱了没？"))=="是的":
        print("孺子可教")
    else:
        print("朽木不可雕也")

#猜数字
import random
num=random.randint(1,10)             #1到10随机来个数
kk=int(input("随机来个数"))
if kk==num:
    print("对")
elif kk<num:
    gg=int(input("小了，第二次来个数"))
    if gg==num:
        print("对了")
    elif gg<num:
        gg=int(input("小了，第三次来个数"))
        if gg==num:
            print("对了")
        elif gg<num:
            print("小了，没机会咯")
        else:
            print("大了，没机会了")
    else:
        gg = int(input("大了，第三次来个数"))
        if gg == num:
            print("对了")
        elif gg < num:
            print("小了，没机会咯")
        else:
            print("大了，没机会了")
else:
    gg = int(input("大了，第二次来个数"))
    if gg == num:
        print("对了")
    elif gg < num:
        gg = int(input("小了，第三次来个数"))
        if gg == num:
            print("对了")
        elif gg < num:
            print("小了，没机会咯")
        else:
            print("大了，没机会了")
    else:
        gg = int(input("大了，第三次来个数"))
        if gg == num:
            print("对了")
        elif gg < num:
            print("小了，没机会咯")
        else:
            print("大了，没机会了")
#干一件事，直到什么为止
i = 0
gg=0
while i<5:
    print("草")
    i+=1


#输入一个小于100的数字，求其到100的和是多少
kk=int(input("输入一个数"))
if kk >=100:
    print("滚你妈的")
else:
    while  kk<=100:
        gg+=kk
        kk+=1
    print(gg)
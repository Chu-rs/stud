#无限次型猜数字

"""
 import random
 num1=random.randint(1,10)
 flag=True
 k=0
 while flag:
     k+=1
     guess_number=int(input("来来来猜个数："))
     if guess_number==num1:
         print("猜中了，答案是%s"%num1)
        把flag设置为False就是为了终止循环
        # flag=False
     else:
         if guess_number<num1:
             print("猜小了，再猜：")
         else:
             print("猜大了，再猜：")
 print("你一共猜了%s"%k,"次")
 print(f"你一共猜了{k}次")#

"""


#输出不换行
print("这是第一行",end='')
print("这是第二行")

#多行字符串进行对齐
print("wello world")
print("hello my dear")

print("hello\tworld")
print("hello\tmy\tdear")           #等效于按了Tab键


  #搞乘法口诀表
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print("\t")#空内容进行换行




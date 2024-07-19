#布尔类型和比较运算符
#表示真和假
#布尔bool
#True表示真1
#False表示假0
kk=10>3
print(f"10>3的结果是：{kk},类型是{type(kk)}")

#==意思是判断是否相等
#！=意思是判断是否不相等
#   还有判断>,>=,<,<=

num1=10
num2=10
print(f":{num1!=num2}")


#if语句

#先定义变量
age=int(input("输入年龄"))
if age >=18:
    print("满十八")
else:
    print("未成年")

like=str(input("输入喜欢小红与否"))
if like=="不喜欢":
    print("追求别人怎么样"    )
elif like!="不喜欢":
    print("但是小红不喜欢你")
print("要不还是小花吧")

xiaohua=str(input())
if xiaohua!="好的":
    print("注孤生")

    #多个条件
do=str(input("现在在干什么"))
if do=="高中":
    print("那就好好准备高考")
elif do=="大学":
    print("好好谈谈恋爱分分手")
elif like=="不喜欢":
    print("可造之才")
else:
    print("傻逼")


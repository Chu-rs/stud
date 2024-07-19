#把待办事项逐个完成的程序
#for 临时变量a in 里面要处理的东西b
#把b里面的东西一个一个取出给a
b="褚自豪是大哥"
for a in b:
    print(a)
print()
################################################
#for循环不能构建无限循环

#数一数有几个a     ：aabaabbaa
b="aabaabbaa"
k=0
for kk in b:
    if kk=="a":
        k+=1
print(f"aabaabbaa里面有{k}个a")

print()
print()


##########################################
"""
range(3)意思是0 1 2，从0开始的；
range(a,b)
获取一个数列，从a开始到b结束，（不含b）
range（a,b,step）
获取一个数列，从a开始到b结束，且中间的步长为step（不含b）
只能搞数字序列
"""
for r in range(1,11,2):
    print(f"{r}\t",end='')
    print()
########################################
"""
for循环变量作用域


for i in range(5):
    print(i)
print(i)            #这里就是虽然可以输出但是不合理的地方,
i是属于for循环里面的变量，却在外部被拿出来输出
"""
#for循环的嵌套作乘法口诀表
i=1
j=1
for i in range(1,10):
    for j in range (1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()

print()
print()
########################
#break中断循环，continue跳过循环
for i in range(1,10):
    if i%2!=0:
        continue
    elif i>5:
        break
    print(i)



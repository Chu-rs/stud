#while循环的遍历
list=['星痕','无畏','清融','久酷','子阳']

def fun1():#没有输入量所以不需要()内的函数
    i=0
    while i<len(list):
        q=list[i]
        print(f"列表元素是:{list[i]}")
        i+=1

fun1()

#for循环的遍历            j是自动遍历+1的


def fun2():
    for j in list:
        print(f"数据是:{j}")

fun2()








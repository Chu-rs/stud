#数据容器
name_list=['周杰伦','刘德华','张学友']
print(name_list)
#一种可以存储多个元素的python数据类型
"""
python中的数据容器：
list（列表）；tuple（元组）；str（字符串），set（集合），dict（字典）

"""
#1.列表定义
list=['星痕','无畏','清融','久酷','子阳',666]
#定义空列表
y=[]
#以[]作为标识
print(list)
############################
#嵌套列表
my_list=[[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))                   #列表是列表型class的
############################
#使用列表的下标索引从列表中取出元素
print(list[3])#list从0开始，所以找出来显示的是‘久酷’
print(my_list[0][1])#取出第一个里面的第二个
#也可以反向取出
print(list[-1])#取出的就是666了
"""
列表的功能——方法（类似函数的东西）
插入元素
删除元素
清空列表
修改元素
统计元素个数
class Student:
    def add(self,x,y):
        return x+y
"""
#查询下标——找不到的话报错ValueError
#语法：列表.index（元素）
d=list.index('清融')#想要知道’清融‘的下标索引是多少
print(d)
print(list.index('清融'))
#以上两个一致

#2.修改下表索引对应的值
list[5]='久凡'
print(list[5])
#直接列表名[索引值]=需要修改的值

#元素插入，在指定下标处插入指定值
#比如在’久酷‘，’子阳‘之间插入’久诚‘       使用   列表名.insert（插入点,插入内容）
m=list.index('久酷')
list.insert(m+1,'久诚')
print(list)
#还有一类叫做元素追加，追加是加到末尾去的
#列表.append(元素)
list.append('尘夏')#直接追加到尾部

print(list)
#########一个不够，追加一批
#列表.extend(其他数据容器)
list.extend(['九尾','小白熊','小胖'])
print(list)
#################两种删除方法：
#语法1          del 列表[对应下标]     语法2 列表.pop(下标)
del list[6]#只能删一个
y=list.index('九尾')
print(y)
list.pop(7)#只能删一个
print(list)
#不通过下标而是通过内容删除
#列表.remove(元素)    移除列表里从左往右第一个匹配元素
list.remove('小白熊') #只能删一个
print(list)
list.extend(['久诚'])###如果是不加[]的('久诚'),输出就变成了'久','诚'
list.extend(['清融','无畏'])
print(list)
##现在统计 无畏 在列表中出现的次数
print(list.count('无畏'))
###########查询列表中元素数量一共多少
print(len(list))

#全部清空
list.clear()
print(list)         #输出就是个空列表[]
































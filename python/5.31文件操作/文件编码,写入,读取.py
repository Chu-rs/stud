"""
UTF-8是通用编码
open(name,mode,encoding)
name要打开目标文件名的字符串且可以包含文件所在的具体路径
mode设置打开的模式,只读,写入,追加
encoding编码格式-----推荐UTF-8
r只读
w覆盖写入
a追加

文件对象.read(读取字长数)
文件对象.readlines()   把整个文件内容进行一次性读取,切返回值是一个列表
且每一行的数据为一个元素'



import time

"""
kk=open("E:\新建 文本文档.txt","r",encoding="UTF-8")
print(type(kk))    #类型:<class '_io.TextIOWrapper'>
#k=kk.read(10)
#print(f"读取十个字节:{k}")
####妈的这也太坑了.只有txt是好用的,docx直接报错
#lin=kk.readlines()#读取全部行封装的列表里,一行一个元素
#print(f"lin的内容:{lin}")  #指针向后偏了

 #######但是如果是readline,没有s情况下是只会读一行

for i in kk:
    print(f"每一行分别是:{i}")

import time
#############文件睡眠:
time.sleep(5)#文件暂停执行5秒

##########解除占用和关闭
kk.close()

###########with open是拿出来以后把原文件关掉的
#这样可以解除不必要的占用
with open("E:\新建 文本文档.txt","r",encoding="UTF-8") as gg:
    for lines in gg:
        print(f"每一行分别是:{lines}")


"""
write的方法并不是真正写入文件里面,而是写到程序的内存里面,
只有调用flush时候才会真正写进去

"""
f = open("E:/text.txt","a",encoding="UTF-8")#把w换成a就可以变成在后面追加

f.write("\n我喜欢你")#内容写入内存
f.flush()#将内容里的写入文件
#但是是清空了再写入

#f.close其实是内置了flush功能了的




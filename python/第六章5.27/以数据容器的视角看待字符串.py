"""
"asdhuf"本身就是一个容器
a的下标是0,s的下标是1

字符串是不可修改的容器
所以修改指定下标元素
字符串[?]="元素",
del字符串[0],字符串.remove(),字符串.pop()
这些都不行

"""
x1="123 * 北 京 信 息 科 技 大 学 *212"
print(x1)
a1=x1[0]
a2=x1[1]
a3=x1[-1]
print(f"这个字符串的前两个字是:{a1}\t{a2},最后一个字符是:{a3}")

########字符串.index()
b=x1.index("北")
print(f"北这个字出现下标{b}")
 ##################字符从替换
 #字符串.replace(字符串1,字符串2)
 #把字符串1里的东西替换成字符串2,得到一个新的字符串
x2=x1.replace("信 息 科 技 ","")
print(f"替换后:{x2}")
#字符串的分割,分割以后变成了列表
x3_list=x1.split(" ")
print(f"切分后成为列表:{x3_list}")
#####字符串规整操作,字符串.strip()去除前后空格
######字符串.strip(字符)去除前后指定字符      是就去除,不管顺序,但是前面不能有东西
x4=x1.strip(" 123")
print(x4)
#######统计字符串里面某字符串出现次数
x5=x1.count("北")
print(f"'北'出现的次数{x5}")
#########字符串长度:
x6=len(x1)
print(f"x1字符串长度:{x6}")







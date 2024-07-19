"""
len()是python的内置函数
但是我们可以自己定义函数
比如我们不用len来统计字长
"""
str="efbol;qwehdop"
k=0
for i in str:
   k+=1
print(f"k的长度是：{k}")

str1="hqwafjklvhqeilvy"
#################################
#现在我们来做个函数
def my_len(kk):
   b=0
   for i in kk:
      b+=1
   print(f"这个字符串{kk}的长度是：{b}")

my_len(str1)

def hanshu(j):
   a=0
   while a<11:
      j+=a
      a+=1
   print(f"这个数字加55是：{j}")
   return
p=1
while p<5:
   hanshu(p)
   p+=1

##########################
def say_hi():
   print("什么玩意儿啊")

#函数定义完成以后需要去调用才能工作
#调用语法：函数名（参数）
say_hi()
###############################################









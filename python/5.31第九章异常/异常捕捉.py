"""
try:
    可能出现异常的代码
except:
    如果发生异常而执行的代码
"""
try:
    open("D:/abc.txt","r",encoding="UTF-8")
except:
    print("sb")


#############捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
###################捕获多个异常
try:
    print(name)
except (NameError,SyntaxError) as e:
    print("出现异常")
    print(e)

#######捕获所有异常
try:
    print("ssbb")
except Exception as e:
    print("异常")
##########没有出现异常的处理
else:
    print("去你妈的")

############这样就没有问题的try的和else的程序都运行了

#还有一个是不管有没有异常我都要运行:
finally:
    print("我爱你")




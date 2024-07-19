"""
python包就是python的文件夹
本质上仍然是模块
使用__init__.py文件

调用时候
import 包名.模块名
包名.模块名.目标函数


科学计算中常用:numpy包
数据分析pandas包
大数据计算中常用pyspark,apache-flink包
图形可视化:matplotlib,pyecharts包
人工智能:tensorflow包
"""





















import my_package.模块1
import my_package.模块2
a=my_package.模块1.x1()
b=my_package.模块2.y1()
print(f"他们的求和结果是:{a+b}")

###########用from导入
from my_package.模块1 import x1 as i

from my_package.模块2 import y1 as j

a=i()
b=j()
print(f"他们的相乘结果是:{a*b}")


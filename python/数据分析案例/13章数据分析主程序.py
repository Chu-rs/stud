"""
某公司现在有两份数据,现在需要对其进行数据分析,
计算每日销售额并且以柱状图表方式进行
一月份的是逗号隔开
二月份是json数据

读取数据        设计类
封装数据对象    封装到类对象里
计算对象         对对象的逻辑对象
绘图           面向对象的绘图


1.设计一个类,可以完成数据封装
2.设计一个抽象类,定义文件读取相关功能,并且使用子类去实现功能
3.读取文件,生成数据对象
4.根据要求进行逻辑计算
5,图形绘制

"""
from 文件读取 import shuju,txt_read,json_read
from 数据定义 import Record

from pyecharts.charts import Bar#柱状图
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt = txt_read("E:/2011年1月销售数据.txt")
json1 = json_read("E:/2011年2月销售数据JSON.txt")

list1:list[Record] = txt.read()
list2:list[Record] = json1.read()
#将两个数据合体
all_list:list[Record] =list1+list2

#开始计算数据
#如何把同一天数据整合一起
#使用字典然后for
data_dict={}
for i in all_list:
    if i.date in data_dict.keys():
        #有记录的,累加即可
        data_dict[i.date]+=i.money
    else:
        data_dict[i.date]=i.money
print(data_dict)

#然后根据数据绘图
bar=Bar()
bar.add_xaxis(list(data_dict.keys())) #添加x轴数据
bar.add_yaxis("销售额",list(data_dict.values()))   #添加y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")    #又构建一个类对象
)

bar.render("每日销售额柱状图.html")




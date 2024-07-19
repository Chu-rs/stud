"""
到折线图了

"""
import json
#打开文件
us_k=open("E:/美国.txt","r",encoding="UTF-8")
us=us_k.read()#读到美国全部内容
jp_k=open("E:/日本.txt","r",encoding="UTF-8")
jp=jp_k.read()#读到日本全部数据
ind_k=open("E:/印度.txt","r",encoding="UTF-8")
ind=ind_k.read()#读到印度全部内容


#去掉不适合的开头
us=us.replace("jsonp_1629344292311_69436(","")
jp=jp.replace("jsonp_1629350871167_29498(","")
ind=ind.replace("jsonp_1629350745930_63180(","")
#去掉不合适的文件的结尾
us=us[:-2]
jp=jp[:-2]
ind=ind[:-2]
#json转python字典
us_zidian=json.loads(us)
print(type(us_zidian))

jp_zidian=json.loads(jp)
print(type(jp_zidian))

ind_zidian=json.loads(ind)
print(type(ind_zidian))

#获取trend key
us_key=us_zidian['data'][0]['trend']
jp_key=jp_zidian['data'][0]['trend']
ind_key=ind_zidian['data'][0]['trend']

#x轴编写,日期
x_us=us_key['updateDate'][:314]
x_jp=jp_key['updateDate'][:314]
x_us=ind_key['updateDate'][:314]


#y轴编写,数据
y_us=us_key['list'][0]['data'][:314]
y_jp=jp_key['list'][0]['data'][:314]
y_ind=ind_key['list'][0]['data'][:314]

#生成图表
#导包,导入line功能构建折线对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
from pyecharts.options import LegendOpts,VisualMapOpts,ToolboxOpts


line=Line()
#添加x轴数据
line.add_xaxis(x_jp)#x轴公用
#添加y轴
line.add_yaxis("美国强奸人数",y_us)
line.add_yaxis("日本强奸人数",y_jp)
line.add_yaxis("印度强奸人数",y_ind)



#全局配置,通过set_global_opts
line.set_global_opts(
    #配置标题         pos_top意思是靠中间多少      pos_bottom意思是靠底部多少
    title_opts=TitleOpts("强奸情况",pos_left="center",pos_bottom="1%"),
    #控制图例   is_show意思是是否展示
    legend_opts=LegendOpts(is_show=True),
    #工具箱
    toolbox_opts=ToolboxOpts(is_show=True),




)





#调用render方法生成图表
line.render()
#关闭文件
us_k.close()
jp_k.close()
ind_k.close()






















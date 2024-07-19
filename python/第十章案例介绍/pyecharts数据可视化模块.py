"""
构建一个折线图
使用全局配置项设置属性
"""
#导包,导入line功能构建折线对象
from pyecharts.charts import Line as k
from pyecharts.options import TitleOpts as g
from pyecharts.options import LegendOpts,VisualMapOpts,ToolboxOpts
#得到折现图对象
kk=k()
#添加X轴数据
kk.add_xaxis(["清融","无畏","久酷","星痕","子阳"])
#添加y轴数据
kk.add_yaxis("kda",[12,10,9,9.9,21])

##两类配置,全局配置----标题,工具箱等等
# 系列配置,针对轴内配置

#全局配置,通过set_global_opts
kk.set_global_opts(
    #配置标题         pos_top意思是靠中间多少      pos_bottom意思是靠底部多少
    title_opts=g("kad情况",pos_left="center",pos_bottom="1%"),
    #控制图例   is_show意思是是否展示
    legend_opts=LegendOpts(is_show=True),
    #工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    #视觉映射
    visualmap_opts=VisualMapOpts(is_calculable=True),

)


#生成
kk.render()









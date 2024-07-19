#这玩意用元组做出来的
from pyecharts.charts import Map
from pyecharts.options import LegendOpts,VisualMapOpts,ToolboxOpts
map=Map()
data=[
    ("北京市",11),
    ("浙江省",12),
    ("广东省",90),
    ("新疆维吾尔自治区",1)
]
map.add("测试地图",data,"china")
#设置全局属性
map.set_global_opts(
#    #视觉映射
#    visualmap_opts=VisualMapOpts(is_calculable=True),
    visualmap_opts=VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":200,"label":"100-500","color":"#990033"}
        ]




    )



    )





map.render()









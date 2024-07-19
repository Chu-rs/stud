

import json
from pyecharts.charts import Map
from pyecharts.options import *
#打开疫情文件赋值给f
f=open("E:/疫情.txt","r",encoding="UTF-8")
data=f.read()#全部读掉
#用完即关掉
f.close()
#取到各省
data_zidian=json.loads(data)#基础数据字典
province_data=data_zidian["areaTree"][0]["children"]
#然后循环各个省拿出数据
shuju_list=[]
for province in province_data:
    province_name=province["name"]             #拿出其中的省份
    if province_name=='北京':
        province_name+="市"
    elif province_name=='重庆':
        province_name+="市"
    elif province_name=="上海":
        province_name += "市"
    elif province_name=="天津":
        province_name+= "市"
    elif province_name=="香港":
        province_name+="特别行政区"
    elif province_name == "澳门":
        province_name += "特别行政区"
    elif province_name == "西藏":
        province_name += "自治区"
    elif province_name == "新疆":
        province_name += "维吾尔自治区"
    elif province_name == "内蒙古":
        province_name += "自治区"
    elif province_name == "宁夏":
        province_name += "回族自治区"
    elif province_name == "广西":
        province_name += "壮族自治区"
    else:
        province_name+="省"
    confirm=province["total"]["confirm"]       #拿出相对应的人数
    shuju_list.append((province_name,confirm)) #把我们要的数据添加到数据列表里
    print(province_name,"\n")

print(shuju_list)
map=Map()
map.add("确诊人数地图",shuju_list,"china")
#设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_piecewise=True,   ####是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "##BBFFFF"},  #淡青色
            {"min": 100, "max": 999, "label": "100-999", "color": "#FF6666"},#橙色
            {"min": 1000, "max":4999 , "label": "1000-4999", "color": "#FF6A6A"}, #淡红
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#8B3A3A"},  #深红
            {"min": 10000, "max": 49999, "label": "10000-49999", "color": "#8B1A1A"},#黑红
            {"min": 100000, "label": "100000+", "color": "#000000"}  #黑色
        ]
    )
)

map.render()









"""
json可以是字典,也可以是列表里面嵌套着字典

"""

#json模块导入
import json
data=[{"清融":18,"kda":8.2},{"无畏":19,"kda":7.1},{"久酷":20,"kda":11}]
#转化为json变量
json_str=json.dumps(data,ensure_ascii=False)#不适应ACSII码,而是直接输出
print(type(json_str))#k的数据类型
print(json_str)
#把json转化为python
s='[{"清融":18,"kda":8.2},{"无畏":19,"kda":7.1},{"久酷":20,"kda":11}]'
json.loads(s)
l=json.loads(s)
print(type(l))
print(l)











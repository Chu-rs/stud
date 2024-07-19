
import json

from 数据定义 import Record

#定义一个抽象类做顶层设计
class shuju:
    def read(self)->list[Record]:
        """读取文件数据,读到的每一条都作为Record的对象
        把他们都封装到list内"""
        pass
    #构建第一个,文件文件的读取器
class txt_read(shuju):

    def __init__(self,path):
        self.path=path#定义成员变量记录文件的路径'



    #复写父类的方法
    def read(self)->list[Record]:
        f=open(self.path,"r",encoding="UTF-8")
        #返回成list,先给个空的
        record_list:list[Record]=[]


        for line in f.readlines():
            line=line.strip()   #消除每一行读到的回车
            data_list=line.split(",")   # 指定逗号为分隔符,分割
            Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])

        f.close()
        return record_list



############################现在处理第二份文件
class json_read(shuju):
    def __init__(self,path):
        self.path=path#定义成员变量记录文件的路径'

    #复写父类的方法
    def read(self)->list[Record]:
        f=open(self.path,"r",encoding="UTF-8")
        #返回成list,先给个空的
        record_list:list[Record]=[]
        for line in f.readlines():

            data_dict=json.loads(line)       #json文件转换为python内部格式
            record=Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list



if __name__=='__main__':
    txt=txt_read("E:/2011年1月销售数据.txt")
    list1=txt.read()
    json1=json_read("E:/2011年2月销售数据JSON.txt")
    list2=json1.read()

    for l in list1:
        print(l)
    for k in  list2:
        print(k)   #给的是内存地址

























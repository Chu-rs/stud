"""
数据定义的类

"""
class Record:

    #构造方法的形式进行定义
    def __init__(self,date,id,money,province):
        self.date=date#日期
        self.id=id#订单id
        self.money=money#订单金额
        self.province=province#订单省份

        #给个魔术方法
    def __str__(self):
        return f"{self.date},{self.id},{self.money},{self.province}"























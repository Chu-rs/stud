"""
多种状态,使用不同的对象
子类去构造,丰富父类
"""
class animal:    #这是抽象类,是空的

    def speak(self):
        pass

#现在构造子类
class dog(animal):
    def speak(self):
        print("汪汪汪")
class cat(animal):
    def speak(self):
        print("猫猫猫")
def kk(animal:animal):
    """
    形成声明要求接收父类对象
    实际传入父类下的子类对象进行工作
父类最定义声明
子类做实际工作
用以获得同一行为不同的状态

    :param animal:
    :return:
    """
    animal.speak()

dog=dog()
cat=cat()

kk(cat)
kk(dog)










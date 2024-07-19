def str_reverse(s):#反转功能函数
    return s[::-1]#反转


def substr(s,x,y):
    """

    :param s: 即将被切片字符串
    :param x: 切片开始下标
    :param y: 切片结束下标
    :return: 切好后返回的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("我很喜欢你"))
    print(substr("我很喜欢你",1,3))






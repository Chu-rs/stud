def print_file_info(file_name):
    """
    将给定路径的文件内容输出到控制台
    :param file_name:即将读取的文件路径
    :return:
    """
    f=None
    try:
        f=open(file_name,"r",encoding="UTF-8")
        content=f.read()
        print("文件全部内容:")
        print(content)
    except Exception as e:
        print(f"文件异常了,原因:{e}")
    finally:
        if f:        #如果f里是None,表示Flase,如果有任何内容,则为Ture
            f.close()
def append_to_file(file_name,data):
    """
    将指定数据追加到指定文件
    :param file_name:指定文件路径
    :param data:指定数据
    :return:
    """
    f=open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("E:/text.txt")
    append_to_file("E:/text.txt","所以,你喜欢我吗?")
    print_file_info("E:/text.txt")


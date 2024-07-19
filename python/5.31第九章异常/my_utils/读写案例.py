import my_utils.字符串模块
from my_utils import 文件处理模块 as kk
print(my_utils.字符串模块.str_reverse("我喜欢你"))
print(my_utils.字符串模块.substr("所以是真的对吧",3,5))

kk.append_to_file("E:/text.txt","真的真的真的")
kk.print_file_info("E:/text.txt")

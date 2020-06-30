'''
功能描述：
1、新建一个类check_tool,继承lianxi类
2、实例化对象hp
3、调用lianxi类中的方法
'''
from unitcase.lianxi import lianxi

class check_tool(lianxi):
    hp=lianxi()
    print(hp.Deduplication1())
    print(hp.Divide())
    print(hp.factorial_list())
    print(hp.Prime_number())





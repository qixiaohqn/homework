'''
'''


#1、位置函数
class function(object):
    def sum(a,b):
        return a+b
    #2、默认函数
    def sum1(a,b=1):
        return a+b

    def add_end(len=[]):
        len.append('end')
        return len

    #3、可变参数 *args
    def calc(*number):
        print(number)
        print(*number)
        sum=0

        for n in number:
            sum+=n
        return n

    #4、关键字参数 **kwargs
    def person(name,age,**kwargs):
        print(name,'age',age,kwargs)



if __name__ == '__main__':
    print(function.sum(1,2))
    print(function.sum1(5,6))
    print(function.add_end())
    print(function.calc(9))
    function.person('xiaohong', 20, sex='fmale')

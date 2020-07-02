#try....except
#一、处理异常：try…except
#1、处理已知异常
from unittest import result


def cacl(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:#已异常
        print("除数不能为0")
#2、处理未知异常，：exception 和BaseException
def cacl1(a,b):
    try:
        print(a / b)
    except BaseException:#未知异常
        print("除数不能为0")

#二、获取异常信息：用as result接收  print(result)
def cacl2(a,b):
    try:
        print(a / b)
    except BaseException as msg:#未知异常
        print(msg)







#三、多个错误信息：用except后跟多个错误类型 (ZeroDivisionError,NameError) as result:
#1、挨个匹配：except的异常类型
def cacll1(a,b):
    try:
        print(a/b)
    except NameError:
        print("该对象未声明")
    except ZeroDivisionError:
        print("除数不能为0")
#2、最终处理，不管有没有抛出异常，都执行finally
def cacll2(a,b):
    try:
        print(a/b)
    except NameError:
        print("该对象未声明")
    except ZeroDivisionError as msg:
        print("msg")
    finally:
        print("程序执行完成")
#3、程序没有抛出异常的时候，执行else'

def call(a,b):
    try:
        print(a/b)
    except NameError as msg:
        print(msg)
    except ZeroDivisionError as msg:
        print(msg)
    except BaseException as msg:
        print(msg)
    else:
        print("程序执行完毕！")





if __name__ == '__main__':
    call(6,100)





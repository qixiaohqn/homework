import _io
def read_data():
    try:
        print(open('/Users/qixiaohan/code/homework/data.tx','r',encoding='UTF-8'))
    except BaseException as msg:
        print(msg)



read_data()
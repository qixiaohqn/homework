#coding utf-8
def read_data():
    f=open("data.tx",'r')
    print(f)

def write_data():
    list1=['\nhello','\nhappy','\nnews','\nBBC']
    f=open('data1.txt','w')
    f.writelines(list1)


if __name__ == '__main__':
    read_data()
    write_data()
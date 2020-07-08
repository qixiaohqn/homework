#coding utf-8
from io import open
def read_data1():
    f=open("data.tx",'r')
    print(f)
    f.close()

def write_data():
    list1=['\nhello','\nhappy','\nnews','\nBBC']
    f=open('data1.txt','w')
    f.writelines(list1)
    f.close()

if __name__ == '__main__':
    read_data1()
    write_data()
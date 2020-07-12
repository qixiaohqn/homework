'''
1、求10阶乘
2、求100以内能被3整除的数，并将作为列表输出
3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
4、求斐波那契数列 1 2 3 5 8 13 ⋯⋯
5、求10000以内的质数
'''



class lianxi(object):
#1、求10阶乘
    def factorial_list(self):
#定义变量，x、i，x存放累加的指，i 自增变量
        x=1
        i=1
        while i<=10:
            x=x*i
            i=i+1
        return x#返回x的值
#2、求100以内能被3整除的数，并将作为列表输出
    def Divide(self):
        list1=[]#定义列表
        for i in range(1,101):
            #被3整除的数等于0
            if i%3==0:
                list1.append(i)
        return list1#返回列表的值

#3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
    def Deduplication1(self):
        list1=[1,2,3,4,3,4,2,5,5,8,9,7]
        list2=[]
        num=0
        for num in list1:
            if num not in list2:
                list2.append(num)
        return list2
    def Deduplication2(self):
        list1=[1,2,3,4,3,4,2,5,5,8,9,7]
        list2=[1,2,3,4,3,4,2,5,5,8,9,7]
        for num in list1:
            if list2.count(num)>1:
               list2.remove(num)
        return list2
#4、求斐波那契数列 1 2 3 5 8 13 ⋯⋯
    def Fibonacci1(self):
        list1=[]

        for i in range(1,10):
            if i==1 or i==2:
               list1.append(i)
            else:
                list1.append(list1[i-2]+list1[i-1])
        return list1
# 5、求10000以内的质数
    def Prime_number1 (self):
        list1=[]
        for i in range (1,20):
            flg=True

            for j in range (2,i):
                if i%j==0:
                    flg=False
                    break
            if flg:
                list1.append(i)
        return list1
    def Prime_number2 (self):
        list1=[]
        for i in range (1,20):
            if i==1 or i==2:
                list1.append(i)
            else:
                for j in range (2,i):
                    if i % j==0:
                        break
                    elif j==i-1:
                     list1.append(i)


        return list1




if __name__ == '__main__':
    a=lianxi()
    print(a.Prime_number2())



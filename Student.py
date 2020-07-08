'''
a、定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程

b、定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程
'''
class Student(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def study(self,course):
        print(self.name+'学习'+course+'课程')

    def study1(self,sno,course):
        print('学号为'+sno+'的学生，'+'学习'+course+'课程')


    def person(self):
        print(self.name+self.age+'岁了')


if __name__ == '__main__':

    h=Student('小米','30')
    h.study('历史')

    s=Student('小米','30')
    s.study1('004','历史')

    h1=Student('小米','30')
    h1.person()


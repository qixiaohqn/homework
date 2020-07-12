class string_lianxi(object):
    def str_capital(self):
        #把字符串的第一个字符大写
        str=input('请输入一串字符：')
        result=str.capitalize()
        print(result)

    def str_count(self):
        # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次
        str=input('请输入一串字符：')
        strs=str.count('e')
        print(strs)



    def str_find(self):
        #输入一个字符，再次输入一个字符串，从下标0开始，查找在字符串里第一个出现的子串
        str=input('请输入一个串字符:')
        print(str.find(input("请输入一个字符串："),1))

    def str_isalpha(self):
        '''
        1、输入的字符串全部都是字母则返回 True
        2、输入非字母则返回 False
        3、输入空格则返回 False
        如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False'''
        str= input('请输入一个字符串：')
        print(str.isalpha())

    def str_isdigit(self):
        '''
        1、输入的字符串全部都是数字则返回 True
        2、输入非数字则返回 False
        3、输入空格则返回 False
        '''
        #如果 string 只包含数字则返回 True 否则返回 False.
        str = input('请输入一个字符串：')
        print(str.isdigit())

    def str_join(self):
        #以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
        str = input('请输入一个字符串：')
        strs= input('请输入一个字符串：')
        print(str.join(strs))
    def str_replace(self):
        #把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
        str1=input('请输入一个字符串：')
        str2=input('请输入一个字符串：')
        print(str1.replace(str2,1))

    def str_split(self):
        print(str.find(input("请输入一个字符串："), 1))
        pass







if __name__ == '__main__':
    str=string_lianxi()
    str.str_replace()

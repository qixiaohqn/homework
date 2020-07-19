import  requests,json
# 示例1：不带参数的get
urlstr = 'http://www.baidu.com/'
res=requests.get(url=urlstr)
print(res.cookies)
#help(requests) #使用help函数就能查看相关注释和案例内容
#示例2：带参数的get
urlstr = 'https://www.wanandroid.com/article/query'
payload={'k':'Android'}
res = requests.get(url=urlstr,params=payload)
print(res.headers)









import requests,json
''' 
       #功能描述
       发送post请求(json形式)
         1.post的body是json类型，有两种方法来传递json数据。
         2.第一种：先导入json模块，用dumps方法转化成json格式。
         3.第二种：使用json参数默认处理成json格式进行传递。
         4.返回结果，传到data里。'''

#示例1：先导入json模块，用dumps方法转化成json格式
urlstr='http://httpbin.org/post'
payload={'qq群名':'selelium+jemter+laodrunner','qq群名':'106014970'}
payload=json.dumps(payload)
r=requests.post(url=urlstr,data=payload)
print(r.text)
print(r.json())


#示例2：使用json参数默认处理成json格式进行传递
urlstr='http://httpbin.org/post'
payload={'qq群名':'selelium+jemter+laodrunner','qq群名':'106014970'}
r=requests.post(url=urlstr,json=payload)
print(r.text)
print(r.json())

#示例3：post登录
urlstr='https://wanandroid.com/user/login'
header={'User-Agent':'Mozilla/5.0'}
payload={'username':'18001036589@163.com','password':'123456'}
r=requests.post(url=urlstr,data=payload,headers=header)
print(r.content)

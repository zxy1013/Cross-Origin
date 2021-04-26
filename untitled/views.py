# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/4/19 20:00
# @ File:views.py
import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# 跨域访问
# 通过后台服务端进行对其他域的请求
def req(request):
    response = requests.get("http://127.0.0.1:5000/newsdetail/1")
    # 设置字节类型
    response.encoding = 'utf-8'
    return render(request,'req.html',{"result":response.text})

# 通过flask的flask-cors第三方扩展
def cor(request):
    return render(request,'cor.html')

# 访问http://www.jxntv.cn/data/jmd-jxtv2.html?callback=list
def jsonp(request):
    return render(request,'jsonp.html')


# jsonp: json with padding
# 创建一个回调函数，然后在远程服务上调用这个函数并且将JSON数据形式作为参数传递，完成回调。将JSON数据填充进回调函数，这就是JSONP的JSON+Padding的含义。
# 打开项目终端 python manage.py runserver 8002
# 访问http://127.0.0.1:8000/jsonp1/ server2打印{'k1': 'v1'} server1打印{"status": 200, "msg": "jsonp2"}
# 所以http://127.0.0.1:8000/jsonp1/ 访问http://127.0.0.1:8002/jsonp2/成功
def jsonp1(request):
    return render(request,'jsonp1.html')

def jsonp2(request):
    ret = {"status": 200, "msg": "jsonp2"}
    func_name = request.GET.get("callback")
    print("{}({})".format(func_name, json.dumps(ret)))
    return HttpResponse(str("{}({})").format(func_name, json.dumps(ret)), content_type='text/javascript')
    # 不加content_type会报错Cross-Origin Read Blocking (CORB) blocked cross-origin response http://127.0.0.1:8002/jsonp2?&callback=callback&_=1618987609564 with MIME type text/html.



# 设置响应头
def jsonp3(request):
    return render(request,'jsonp3.html')

def jsonp4(request):
    obj = JsonResponse([ '西游记2', '三国演义2', '水浒传2' ], safe=False)
    # 下面这个响应头信息是告诉浏览器，不要拦着，我就给它，"*"的意思是谁来请求我，我都给
    obj[ "Access-Control-Allow-Origin" ] = "http://127.0.0.1:8000"
    # 只有这个ip和端口来的请求，我才给他数据，其他的请求浏览器帮我拦着
    return obj


# django的第三方扩展django-cors-headers  配置方法在readme中
def cors1(request):
    return render(request,'cors1.html')

def cors2(request):
    obj = JsonResponse([ '西游记2', '三国演义2', '水浒传2' ], safe=False)
    return obj
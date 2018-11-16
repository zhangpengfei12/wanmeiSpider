#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib.request
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
x = 0


def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):

    imgre = re.compile('<img id="PicBig" src="(.*?)" width="400" border="0" />')     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    chanpingdaihao = re.compile('<span id="Label_ProCode" class="txt_5a5a5a_16_30">(.*?)</span>')

    html = html.decode('utf-8')
    html = html.replace("*","")
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    chanpingdaihaolist = re.findall(chanpingdaihao,html)  
    print(imglist,chanpingdaihaolist)
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    global x

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'D:\wanmei\%s.jpg' % chanpingdaihaolist)
        print(x)
        x+=1

for i in range(10):
    try:
        html = getHtml("http://www.perfect99.com/product/ProDetail"+ str(i) +".html")
        getImg(html)
    except Exception as e:
        print("此页无图")
    
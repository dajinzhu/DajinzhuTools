#作者： 陈锡
import urllib.request ,sys
import re
import calendar
from turtle import*
import time
import json
import tkinter as tk
import requests




def close():
    print('结束程序，再见！')

def tianqi():
    def get_html(url):  
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER',
                   'Cookie': 'Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1551710200,1551710796; '
                             'vjuids=-420397a32.1654b696dba.0.51e70be3fe1888; '
                             'vjlast=1534568525.1542882831.23; '
                             'f_city=%E6%8F%AD%E9%98%B3%7C101281901%7C; '
                             'Wa_lvt_1=1551710201,1551710796; '
                             'Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1551712743; '
                             'Wa_lpvt_1=1551711053'
                   }

        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text


    def get_html1(url, city_id):  # 向网站发送请求，代码格式固定
        # 请求头
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER',
                   'Cookie': 'Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1551710200,1551710796; '
                             'vjuids=-420397a32.1654b696dba.0.51e70be3fe1888; '
                             'vjlast=1534568525.1542882831.23; '
                             'f_city=%E6%8F%AD%E9%98%B3%7C101281901%7C; '
                             'Wa_lvt_1=1551710201,1551710796; '
                             'Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1551712743; '
                             'Wa_lpvt_1=1551711053',
                   'Host': 'd1.weather.com.cn',
                   'Connection': 'keep-alive',
                   'Accept': '*/*',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en;q=0.3,en-US;q=0.2',
                   'Cache-Control': 'no-cache',
                   'Pragma': 'no-cache',
                   'Referer': 'http://www.weather.com.cn/weather1d/%s.shtml' % city_id
                   }

        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text


    def get_city_id(name):  # 获取城市的id
        # 通过分析，城市id信息在这个url中，
        url = "http://toy1.weather.com.cn/search?cityname=%s&callback=success_jsonpCallback&_=1551710682616" % name
        html = get_html(url)  # 获取页面信息
        pattern = "([0-9]+)~[a-z]+~%s" % name  # pattern格式，匹配城市id
        search_id = re.search(pattern, html)
        if search_id:  # 如果有这个城市的话，就能匹配到
            city_id = search_id.group(1)  # 获取城市id
            return city_id  # 返回城市id
        else:
            return None  # 没有这个城市则返回空


    def crawl_weather(city_id):  # 爬取城市天气信息
        # 通过分析，城市天气信息在这个url中
        url = "http://d1.weather.com.cn/sk_2d/%s.html?_=1551712744319" % city_id
        html = get_html1(url, city_id)  # 获取页面信息
        value = re.search("=(.+)", html).group(1).strip()  # 获取标准json
        value = json.loads(value)  # 载入json
        city = value.get("cityname")  # 获取天气基本信息
        temp = value.get("temp")
        wind = value.get("WD")
        wind_level = value.get("WS")
        wet_percent = value.get("SD")
        weather = value.get("weather")
        pm25 = value.get("aqi")
        update_time = value.get("date") + " " + value.get("time")
        # 返回
        return city, temp, wind, wind_level, wet_percent, weather, pm25, update_time


    def generate_information():  # 将获取的信息显示到界面上
        try:
            city_name = city_entry.get()  # 获取输入框中的字符串
            city_id = get_city_id(city_name)  # 获取城市id
            # 获取城市天气信息， 若没有这个城市，则会出错，所以用try-except
            city, temp, wind, wind_level, wet_percent, weather, pm25, update_time = crawl_weather(city_id)
            shtext.delete(0.0, 'end')  # 清除界面
            # 显示在界面上
            shtext.insert('insert', "地区：%s\n" % city)
            shtext.insert('insert', "天气：%s\n" % weather)
            shtext.insert('insert', "温度：%s度\n" % temp)
            shtext.insert('insert', "湿度：%s\n" % wet_percent)
            shtext.insert('insert', "风向：%s\n" % wind)
            shtext.insert('insert', "风力：%s\n" % wind_level)
            shtext.insert('insert', "PM2.5：%s\n" % pm25)
            shtext.insert('insert', "更新时间：%s\n" % update_time)
        except:
            # 出错则显示相应信息
            shtext.delete(0.0, 'end')  # 清除界面
            shtext.insert('insert', "没有--%s--的天气信息。\n输入一个临近地区的名字吧\n" % city_name)


    # 生成主界面
    windows = tk.Tk()
    windows.title('金猪天气')
    windows.geometry('440x290')
    # 定义字符串，在后面有用
    str1 = tk.StringVar()
    # 建立一个框
    shframe1 = tk.Frame(height=100, width=100, borderwidth=1)
    shframe1.grid(row=0, column=0, sticky='W', padx=1)
    # 显示标签
    city_label = tk.Label(shframe1, text="地区：")
    city_label.grid(row=0, column=0, sticky="W")
    # 城市输入框
    city_entry = tk.Entry(shframe1, textvariable=str1, width=20, borderwidth=3)
    city_entry.grid(row=0, column=1, sticky="W")
    # 确定框
    tk.Button(shframe1, text='搜索', borderwidth=3, command=generate_information) \
            .grid(row=0, column=3, columnspan=10, sticky='E', pady=10)
    # 显示信息-------------------------------------------------------------------
    # 建立一个框
    shframe = tk.LabelFrame(height=800, width=1050, text='天气信息', borderwidth=5)
    shframe.grid(row=1, column=0, sticky='W', padx=0)
    # 显示文本框
    shtext = tk.Text(shframe, height=15, width=60)
    shtext.grid(row=3, column=1)

    windows.mainloop()




























def yueli():
    print('---------------------------------')
    yy = int(input("输入年份: "))
    mm = int(input("输入月份: "))


    print(calendar.month(yy,mm))





def wendu():
    print('---------------------------------')
    celsius = float(input('输入摄氏温度: '))
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))

def gys():
    print('---------------------------------')
    def hcf(x, y):
       """该函数返回两个数的最大公约数"""

       # 获取最小值
       if x > y:
           smaller = y
       else:
           smaller = x

       for i in range(1,smaller + 1):
           if((x % i == 0) and (y % i == 0)):
               hcf = i

       return hcf


    # 用户输入两个数字
    num1 = int(input("输入第一个数字: "))
    num2 = int(input("输入第二个数字: "))

    print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))

def jjcfb():
    print('---------------------------------')
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(j, i, i*j), end='')
        print()


def xzpj():
    def nose(x,y):#鼻子
        penup()#提起笔
        goto(x,y)#定位
        pendown()#落笔，开始画
        setheading(-30)#将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
        begin_fill()#准备开始填充图形
        a=0.4
        for i in range(120):
            if 0<=i<30 or 60<=i<90:
                a=a+0.08
                left(3) #向左转3度
                forward(a) #向前走a的步长
            else:
                a=a-0.08
                left(3)
                forward(a)
        end_fill()#填充完成

        penup()
        setheading(90)
        forward(25)
        setheading(0)
        forward(10)
        pendown()
        pencolor(255,155,192)#画笔颜色
        setheading(10)
        begin_fill()
        circle(5)
        color(160,82,45)#返回或设置pencolor和fillcolor
        end_fill()

        penup()
        setheading(0)
        forward(20)
        pendown()
        pencolor(255,155,192)
        setheading(10)
        begin_fill()
        circle(5)
        color(160,82,45)
        end_fill()

    def head(x,y):#头
        color((255,155,192),"pink")
        penup()
        goto(x,y)
        setheading(0)
        pendown()
        begin_fill()
        setheading(180)
        circle(300,-30)
        circle(100,-60)
        circle(80,-100)
        circle(150,-20)
        circle(60,-95)
        setheading(161)
        circle(-300,15)
        penup()
        goto(-100,100)
        pendown()
        setheading(-30)
        a=0.4
        for i in range(60):
            if 0<=i<30 or 60<=i<90:
                a=a+0.08
                lt(3)
                fd(a)
            else:
                a=a-0.08
                lt(3)
                fd(a)
        end_fill()

    def ears(x,y): #耳朵
        color((255,155,192),"pink")
        penup()
        goto(x,y)
        pendown()
        begin_fill()
        setheading(100)
        circle(-50,50)
        circle(-10,120)
        circle(-50,54)
        end_fill()

        penup()
        setheading(90)
        forward(-12)
        setheading(0)
        forward(30)
        pendown()
        begin_fill()
        setheading(100)
        circle(-50,50)
        circle(-10,120)
        circle(-50,56)
        end_fill()

    def eyes(x,y):#眼睛
        color((255,155,192),"white")
        penup()
        setheading(90)
        forward(-20)
        setheading(0)
        forward(-95)
        pendown()
        begin_fill()
        circle(15)
        end_fill()

        color("black")
        penup()
        setheading(90)
        forward(12)
        setheading(0)
        forward(-3)
        pendown()
        begin_fill()
        circle(3)
        end_fill()

        color((255,155,192),"white")
        penup()
        seth(90)
        forward(-25)
        seth(0)
        forward(40)
        pendown()
        begin_fill()
        circle(15)
        end_fill()

        color("black")
        penup()
        setheading(90)
        forward(12)
        setheading(0)
        forward(-3)
        pendown()
        begin_fill()
        circle(3)
        end_fill()

    def cheek(x,y):#腮
        color((255,155,192))
        penup()
        goto(x,y)
        pendown()
        setheading(0)
        begin_fill()
        circle(30)
        end_fill()

    def mouth(x,y): #嘴
        color(239,69,19)
        penup()
        goto(x,y)
        pendown()
        setheading(-80)
        circle(30,40)
        circle(40,80)

    def setting():          #参数设置
        pensize(4)
        hideturtle()        #使乌龟无形（隐藏）
        colormode(255)
        color((255,155,192),"pink")
        setup(840,500)
        speed(10)

    def main():
        setting()           #画布、画笔设置
        nose(-100,100)      #鼻子
        head(-69,167)       #头
        ears(0,160)         #耳朵
        eyes(0,140)         #眼睛
        cheek(80,10)        #腮
        mouth(-20,30)       #嘴
        done()

    if __name__ == '__main__':
    	main()

    elif kaiqi == "0" :
        close()
    else :
        print('错误输入！')


print('欢迎来到大金猪工具箱！')
print('你的名字？')
prompt = '>'
name = input(prompt)
print(f'好了，你的名字是 {name} !')
print(f'{name}，你准备好了吗？开始大金猪万能工具箱！')
print('按1开始 按0结束。')
print('---------------------------------')
kaiqi = input(prompt)
if kaiqi == "1" :
    print('你已进入大金猪工具箱。你需要什么工具？')
    print('---------------------------------')
    print('1.金猪天气')
    print('2.金猪月历')
    print('3.摄氏温度转华氏温度')
    print('4.最大公因数')
    print('5.九九乘法表')
    print('6.小猪佩奇')
    print('---------------------------------')
    xuanze1 = input('请输入序号：')
    if xuanze1 == "1" :
        tianqi()
    if xuanze1 == "2" :
        yueli()
    if xuanze1 == "3" :
        wendu()
    if xuanze1 == "4" :
        gys()

    if xuanze1 == "5" :
        jjcfb()
    if xuanze1 == "6" :
        xzpj()




elif kaiqi == "0" :
    close()
else :
    print('错误输入！')

def jx():
    print('---------------------------------')
    print('继续吗？')
    print('按1继续 按0结束。')
    kaiqi = input(prompt)
    if kaiqi == "1" :
        print('---------------------------------')
        print('1.天气预报')
        print('2.金猪月历')
        print('3.摄氏温度转华氏温度')
        print('4.最大公因数')
        print('5.九九乘法表')
        print('6.小猪佩奇')
        print('---------------------------------')
        xuanze1 = input('请输入序号：')
        if xuanze1 == "1" :
            tianqi()
        if xuanze1 == "2" :
            yueli()
        if xuanze1 == "3" :
            wendu()
        if xuanze1 == "4" :
            gys()
        if xuanze1 == "5" :
            jjcfb()
        if xuanze1 == "6" :
            xzpj()
jx()
jx()
jx()
jx()
jx()
jx()
jx()
jx()
input()

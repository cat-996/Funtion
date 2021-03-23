#使用 turtle 库绘制轮廓颜色为红色（red）、填充颜色为粉红色（pink）的心形图形，效果如下图所示。阅读程序框架，补充横线处代码。
from turle import *
color('red','pink')
begin_fill()
left(135)
fd(100)
rigth(180)
circle(50,-150)
left(90)
circle(50,-150)
right(100)
fd(100)
end_fill()
done()

#使用 turtle 库绘制红色五角星图形，效果如下图所示。阅读程序框架，补充横线处代码。
from turtle import *
setup(400,400)
penup()
goto(-100,50)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(200)
    right(144)
end_fill()
hideturtle()
done()

#使用 turtle 库绘制正方形螺旋线，效果如下图所示。阅读程序框架，补充横线处代码。
import turtle 
n = 10
for i in range(1,10,1):
    for j in [90,180,-90,0]:
        turtle.seth(j)
        turtle.fd(n)
        n += 5

#使用 turtle 库绘制简单城市剪影图形，效果如下图所示。阅读程序框架，补充横线处代码。
import turtle
turtle.setup(800,300)
turtle.penup()
turtle.fd(-350)
turtle.pendown()
def DrawLine(size):
    for angle in [0,90,-90,-90,90]:
        turtle.left(angle)
        turtle.fa(size)
for i in [20,30,40,50,40,30,20]:
    DrawLine(i)
turtle.hideturtle()
turtle.done()

#使用 turtle 库绘制同心圆图形，效果如下图所示。阅读程序框架，补充横线处代码。
for turtle as t 
def DrawCctCircle(n):
    t.pendown()
    t.goto(0,-n)
    t.pendown()
    t.cricle(n)
for i in range(20,100,20):
    DrawCctCircle(i)
t.hideturtle()
t.done()

#使用 turtle 库绘制钢琴键示意图形，效果如下图所示。阅读程序框架，根据注释补充横线处代码。
import turtle as t 
t.setup(500,300)
t.penup()
t,goto(-150,-50)
t,pendown()
def Drawrect():
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.penup()
    t.left(90)
    t.fd(42)
    t.pendown()
for i in range(7):
    Drawrect()
t.penup()
t.goto(-150,0)
t.pendown
def DrawRectBlack():
    t.color('black')
    t.begin_fill()
    t.fd(30)
      t.left(90)
    t.fd(70)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(40)
    t.pendown()
DrawRectBlack()
DrawRectBlack()
DrawRectBlack()
t.hideturtle()
t.done()

#使用 turtle 库绘制叠加等边三角形，效果如下图所示。阅读程序框架，补充横线处代码。
import turtle
turtle.pensize(2)
turtle.color('red')
turtle.forword(160)
turtle.seth(120)
turtle.fd(160)
turtle.penup()
turtle.seth(0)
turtle.pendown()
turtle.seth(60)
turtle.fd(80)
turtle.seth(180)
turtle.fd(80)
turtle.seth(-60)
turtle.fd(80)
turtle.hideturtle()
turtle.done()

#使用 turtle 库绘制八角星形，效果如下图所示。阅读程序框架，补充横线处代码。
import turtle as t 
t.colormode(255)
t.color(255,251,0)
t.begin_fill()
for x in range(1,9):
    t.forward(200)
    t.left(255)
t.end_fill()
t.hideturtle()
t.done()

#使用 turtle 库绘制5种多边形，效果如下图所示。阅读程序框架，补充横线处代码。
from turtle import *
for i in range(5):
    penup()
    goto(-200+100*i,-50)
    pendown()
    circle(40,step=3+i)
done()

#使用 turtle 库绘制树图形，效果如下图所示。阅读程序框架，补充横线处代码。
import turtle as t 
def tree(length,level):
    if level <= 0:
        return
    t.forward(length)
    t.left(45)
    tree(0.6*length,level-1)
    t.right(90)
    tree(0.6*length,level-1)
    t.left(45)
    t.backward(length)
    return
t.pensize(3)
t.color('green')
t.left(90)
tree(100,6)

#获得输入正整数 N，计算 1 到 N 之间所有奇数的平方和，不含 N，直接输出结果。本题不考虑输入异常情况
N =eval(input())
s = 0
for i in range (1,N)
    if i%2 ==1:
        s+= i**2
print(s)

#获得输入正整数 N，判断 N 是否为质数，如果是则输出 True，否则输出 False。本题不考虑输入异常情况
N = eval(input())
if N == 1 :
    flag = False
    print(flag)
else:
    flag = True 
    for i in range(2,N):
        if N % i == 0
            flag = False
            break
    print(flag)

 #获得输入正整数 N，计算各位数字的平方和，直接输出结果。本题不考虑输入异常情况。 
N = input()
s = 0
for i in N :
    s += eval(i)**2
print(s)

#循环从用户处获得一组数据，直到用户直接输入回车退出，打印输出所有数据的和。本题不考虑输入异常情况。 
s = input("请输入一个整数:")
s = 0
while N != "":
    s += eval(N)
    N = input("请输入一个整数:")
print(s)

#编写程序从用户处获得一个不带数字的输入，如果用户输入中含数字，则要求用户再次输入，直至满足条件。打印输出这个输入。 
while True:
    N = input("请给出一个不带数字的输入:")
    flag = True 
    for c in N :
        if c = "123456789":
            flag = False 
            break
    if flag:
        break
print(N)
        
#考虑异常情况，编写程序从用户处获得一个全数字（可以含小数点或复数标记）输入，如果用户输入不符合，则要求用户再次输入，直至满足条件。打印输出这个输入。 
while True:
    try:
        N = input("请给出一个全数字输入:")
        print(eval(N))
        break
    except:
        pass

#不考虑异常情况，编写程序从用户处获得一个浮点数输入，如果用户输入不符合，则要求用户再次输入，直至满足条件。打印输出这个输入。
while True:
    N = input("请给出一个浮点数:")
    if type(eval(N)) = type(1.0):
        print(eval(N))
        break

#考虑异常情况，编写程序从用户处获得一个浮点数输入，如果用户输入不符合，则要求用户再次输入，直至满足条件。打印输出这个输入。
while True:
    try:
        N = input("请给出一个浮点数:")
        if type(eval(N)) == type(1.0):
            print(eval(N))
            break
        except:
            pass 

#输出如下数列在 1000000 以内的值，以逗号分隔：k(0)= 1, k(1)=2, k(n) = k(n–1)2 + k(n–2)2，其中，k(n) 表示该数列。      
a,b = 1,2 
ls = []
ls.append(str(a))
while b < 1000*1000:
    a,b = b,a**2+b**2
    ls.append(str(a))
print(",",join(ls))

#编写程序随机产生 20 个长度不超过 3 位的数字，让其首尾相连以字符串形式输出，随机种子为 17 
import random as r 
r.seed(17)
s = ""
for i in range(20)
    s +=(r.randint(0.999))
print(s)

#使用turtle库绘制如下图的花形图形，效果如下图所示。
import turtle 
for i in range(4):
    turtle.rigth(90)
    turtle.circle(50,180)
#使用turtle库绘制如下图的星形图形，效果如下图所示。
import turtle
for i in range(4)
    turtle.circle(-90,90)
    turtle.rigth(180)
#使用turtle库绘制如下图的类斯洛克图形，效果如下图所示
import turtle
    #绘制边长为20的圆形
def drawCircle():
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.fd(40)

#绘制n层的
def drawRowCircle(n):
    for j in range(n,1,-1):
        for i in range(j):
            drawCircle()
        turtle.fd(-j*40,-20)
        turtle.right(90)
        turtle.fd(40)
        turtle.left(90)
        turlte.fd(40)
    drawCircle()
#调用函数绘制图形
drawRowCircle(5)
turtle.hideturtle()
turtle.done()

#使用turtle库绘制如下图的领结图形，效果如下图所示。
from turtle import *
pensize(6)
penup()
goto(-100,-50)
pendown()
fillcolor("red")
begin_fill()
goto(-100,50)
goto(100,-50)
goto(100,50)
goto(-100,-50)
penup()
goto(-10,0)
pendown()
right(90)
circle(10,360)
end_fill()
hideturtle()
done()

#使用turtle库绘制如下图的图形，效果如下图所示。
import turtle 
def Draw()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.end_fill()   

for i in range(3):
    Draw()
turtle.hideturtle()
turtle.done()

import turtle
r = 20
head = 90
for i in range(3):
    turtle.seth(head)
    turtle.circle(r)
    r = r + 20
r = 20
head = 270
for i in range(3):
    turtle.seth(head)
    turtle.circle(r)
    r = r + 20
turtle.done()

#使用turtle库的turtle.fd()函数和turtle.seth()函数绘制螺旋状类正方形，正方形边长从1像素开始，第一条边从0º方向开始，效果如下图所示。
import turtle 
d = 0
k = 1
for j in range (10):
    for i in range(4):
        turtle.fd(k)
        d += 91
        turtle.seth(d)
        K += 4
turtle.done()

#使用turtle库的turtle.fd()函数和turtle.seth()函数绘制嵌套五边形，边长从1像素开始，第一条边从0º方向开始，边长按照3个像素递增，效果如下图所示。
import turtle
edge = 5
d = 0
k = 1
for j in range(10):
    for i in range(edge):
        turtle.fd(k)
        d += edge/5
        turtle.seth(d)
        k += 3
turtle.done()

#使用turtle库绘制由边长为100像素的菱形构成的六角雪花形状，效果如下图所示。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
import turtle 
def Draw():
    turtle.begin_fill()
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(100)
    turtle.end_fill()
for i in range(3):
    turtle.fillcolor("green")
    Draw()
turtle.left(60)
for i in range(3):
    turtle.fillcolor("blue")
    Draw()
turtle.hideturtle()
turtle.done()

#使用turtle库的绘制十二个花瓣的图形，效果如下图所示。
import turtle 
turtle.fillcolor('yellow')
turtle.begin_full()
for i in range (12):
    turtle.circle(-90,90)
    turtle.right(120)
turtle.end_fill()
turtle.hideturtle()
turtle.done()

#请实现冒泡排序法。冒泡排序（Bubble Sort）的基本步骤是：依次比较相邻的两个数，将小数放在前面，大数放在后面。即在第一趟：首先比较第1个和第2个数，将小数放前，大数放后。
#然后比较第2个数和第3个数，将小数放前，大数放后，如此继续，直至比较最后两个数，将小数放前，大数放后。
ls = [23,41,32,12,56,76,35,67,89,44]
print(ls)
def bub_sort(s_list):
    for i in range(len(s_list)-1):
        is_change = True
        for j in range(len(s_list)-1-i):
            if s_list[j] > s_list[j+1]:
                s_list[j],s_list[j+1] = s_list[j+1],s_list[j]
                is_change = False
        if is_change:
            break
    return s_list
bub_sort(ls)
print(ls)

#使用字典和列表型变量完成某课程的考勤记录统计，某班有74名同学，
#名单由考生目录下文件Name.txt给出，某课程第一次考勤数据由考生目录下文件1.csv给出。不考虑旁听学生的签到数据。请求出第一次缺勤同学的名单。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
with open("1.csv","r",encoding = "utf-8") as fo:
    foR = fo.readlines()
ls = []
for line in foR:
    line = line.replace("\n","")
    is.append(line.split(","))
#从name中读取学生黑名单
with open("Name.txt","r",encoding = "utf-8") as foName:
    foNnameR = foName.readlines()
lsAll = [] 
for line in foNameR:
    line = line.replace("\n","")
    lsall.append(line)
#求第一次缺勤同学的黑名单
for l in ls:
    if l[0] in lsAll:
        lsAll.remove(l[0])
#print第一次缺勤的同学
for l in lsAll:
    print(l,end=" ")

#请对《阿甘正传-网络版》进行中文分词，排除单个字符的分词结果，输出排序后的前10的词语。本题目不支持在线评阅
import jieba
txt = open("阿甘正传-网络版.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts={}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
for i in range(10):
    word(count = items[i])
    print("{0}:{1}",format(word,count))

#从键盘输入一些字符，逐个把它们写到指定的文件，直到输入一个@为止。请完善代码。
filename = input ("请输入文件名:\n")
fp = open(filename,"w")
ch = input("请输入字符串:\n")
while ch != '@':
    if '@' in ch:
        t = ch.find("@")
        fp.writ(ch[0:t])
    else:
        fp.wirte(ch + " ")
    ch = input("")
fp.close()

#求出一组数：1080,750,1080,750,1080,850,960,2000,1250,1630,1080,1800,1080,2100,1080,1450,2500,560,1080,560中的众数及出现频率。众数是指出现次数最多的数。
ls=[1080,750,1080,750,1080,850,960,2000,1250,1630,1080,1800,\
1080,2100,1080,1450,2500,560,1080,560]
counts ={}
for num in ls:
    counts[num] = counts.get(num,0)+ 1
items = list(counts.items())
items.sort(key = lambda x:[1],reverse = True)
num,count = items[0]
print("众数为{},出现频率为{}。".format(num,count))


#编写代码完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

#(1) 建立字典d，包含内容是："中文":101, "英文":202, "法文":203, "德文":204, "韩文":206。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

#(2) 向字典中添加键值对"日文":205。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

#(3) 修改"中文"对应的值为201。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

#(4) 删除"韩文"对应的键值对。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

#(5) 打印字典d全部信息，参考格式如下。
d = {"中文":101,"英文":202,"法文":203,"德文":204,"韩文":206}
d["日文"] = 205
d["中文"] = 201
del d["韩文"]
for key in d:
    print("{}:{}".format(d[key],key))

#计算a中各元素与b逐项乘积的累加和。
a = [[11,22,33], [44,55,66], [77,88,99]]
b = [33,66,99]
s = 0
for c in a:
    for j in range(3):
        s += c[j]*b[j]
print(s)

#补充如下代码，计算向量a与向量b的乘积，即对应元素乘法的累加和，并将结果输出。
a = [11,22,33,44,55,66,77,88,99]
b = [33,66,99,22,55,88,11,44,77]
s = 0
for i in range(len(a)):
    s += a[i] * b[i]
print(s)

#列表ls中存储了我国39所985高校所对应的学校类型，请以这个列表为数据变量，完善Python代码，统计输出各类型的数量。
ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", \
    "综合", "综合", "师范", "理工", "综合", "理工", "综合", "综合", \
    "综合", "综合", "综合", "理工", "理工", "理工", "理工", "师范", \
    "综合", "农林", "理工", "综合", "理工", "理工", "理工", "综合", \
    "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
d = {}
for word in ls:
    d[word] = d.get(word, 0) +1
for k in d:
    print("{}:{}".format(k,d[k]))

#字典d中存储了我国42所双一流高校及所在省份的对应关系，请以这个列表为数据变量，完善Python代码，统计各省份学校的数量。
d = {"北京大学":"北京", "中国人民大学":"北京","清华大学":"北京",\
"北京航空航天大学":"北京","北京理工大学":"北京","中国农业大学":"北京",\
"北京师范大学":"北京","中央民族大学":"北京","南开大学":"天津",\
"天津大学":"天津","大连理工大学":"辽宁","吉林大学":"吉林",\
"哈尔滨工业大学":"黑龙江","复旦大学":"上海", "同济大学":"上海",\
"上海交通大学":"上海","华东师范大学":"上海", "南京大学":"江苏",\
"东南大学":"江苏","浙江大学":"浙江","中国科学技术大学":"安徽",\
"厦门大学":"福建","山东大学":"山东", "中国海洋大学":"山东",\
"武汉大学":"湖北","华中科技大学":"湖北", "中南大学":"湖南",\
"中山大学":"广东","华南理工大学":"广东", "四川大学":"四川",\
"电子科技大学":"四川","重庆大学":"重庆","西安交通大学":"陕西",\
"西北工业大学":"陕西","兰州大学":"甘肃", "国防科技大学":"湖南",\
"东北大学":"辽宁","郑州大学":"河南", "湖南大学":"湖南", "云南大学":"云南", \
"西北农林科技大学":"陕西", "新疆大学":"新疆"}
ls = list(d.values())
dc = {]
for word in ls:
    dc[word] = dc.get(word, 0) + 1
for k in dc:
    print("{}:{}",format(k,dc[k]))
    

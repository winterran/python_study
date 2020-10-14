# -*- coding: utf-8 -*-
'''
Created on 2020��3��28��
@author: Administrator

'''
import os
import requests


#本部分用于os、requests外部库调用的测试

print(os.getcwd())
age=3**2   #**是幂函数的表示法
name=input('姓名：')
print("{0} was {1} years old.", format(name,str(age)))
print(id(name),type(name),id(age),type(age)) #显示变量的内存地址、变量类型
print(name + ' was ' + str(age) +' years old.')


'''
r=requests.get('http://www.google.com')
print(r.url)
print(r.encoding)
print(r.text)
'''



#本部分用于批量改文件名，将文件名中第二个“-”之后至“.mp4”之前的字符串删掉
'''
path="E:\BDdownloads\【曾贤志】从零基础开始用Python处理Excel数据"    # path=input('请输入文件路径(结尾加上/)：')

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

n=0

for i in fileList:

    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符

    #设置新文件名
    mm1 = oldname.find("-")   #找到第一个“-”
    oldname1=oldname[:mm1+1]    #取第一个“-”及前面的字符串
    oldname2=oldname[mm1+1:]  #取第一个“-”后面的字符串

    mm2=oldname2.find("-")    #找到第二个“-”
    if mm2>0:
        oldname3=oldname2[:mm2]+'.mp4'    #取第二个“-”前面的字符串
    else:
        oldname3 = oldname2

    newname=oldname1+oldname3  #取第二个“-”前面的字符串作为新文件名

    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)

    n+=1
'''

#本部分用于测试数据类型转换
'''
num=input('请输入分数：')
num=float(num)
num/=2
print('你的最后得分为：%f 分'%num)
'''

#本部分测试numpy的数组功能，数据分析与展示（5小时学会Python 数据分析与展示(2020年版)）
#进度（2:43:32 / 5:44:15 3.2_单元4：Matplotlib库入门）

import numpy as ny
import matplotlib.pyplot as plt
import pandas as pd

'''
#numpy入门
a=ny.arange(24).reshape((2,3,4))
print(a)
a.mean()
print(a)
a=a/a.mean()
print(a)
'''


'''
#matplotlib入门  (#单多行注释就一个组合键：选中+Ctrl+/)
# plt.plot([3,1,4,5,2])
# plt.ylabel("grade")
# plt.savefig('test',dpi=600) #PNG文件
# plt.show()
c=ny.arange(0.0,5.0,0.02)
plt.plot(c,ny.cos(2*ny.pi*c),'r--')
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=25,color='green')
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=25)
plt.title(r'正弦波实例 $y=cos(2\pi x)$',fontproperties='SimHei',fontsize=25)
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show()
'''

'''
#pandas库入门
b1=pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
b2=pd.DataFrame(ny.arange(12).reshape(3,4))
b3=pd.Series(ny.arange(4))
print(b1)
print(b2)
print(b2>b3)
print(b3)
print(b3>0)
b4=b2.sort_index(ascending=False)
print(b4)
b5=pd.DataFrame(b4,index=[1,2,0])
print(b5)
b6=b5.sort_index()
b7=b6.sort_index(axis=1,ascending=False)
b8=b7.sort_values(2,ascending=False)
print(b6)
print(b7)
print(b8)
print(b8.sum(),b8.count(),b8.mean(),b8.median(),b8.var(),b8.std(),b8.min(),b8.max())
print(b8.describe())
print(b8.describe()[2])
print(type(b8.describe()), b8.describe()[1])
print(b8.cumsum(),b8.cumprod(),b8.cummin(),b8.cummax())
print(b8,b8.rolling(2).sum())
'''

'''
#摄氏度与华氏度之间的转换
for i in range(3):
    val=input("请输入带温度表示符号的温度值（例如：32C-摄氏度，28F-华氏度）：")
    if val[-1] in ['C','c']:
        f=1.8*float(val[0:-1])+32
        print("转换后的温度为：%.2fF"%f)
    elif val[-1] in ['F','f']:
        c=(float(val[0:-1])-32)/1.8
        print("转换后的温度为：%.2fC" %c)
    else:
        print("输入有误")

'''

'''
import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()
'''
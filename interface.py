import tkinter as tk
from tkinter import*
import math 
import time
import snap7
import read
import tkinter.filedialog

global dict_1
global dict_2
global list1
dict_1={'Ipaddress':'192.168.2.10','link_signal':False,'xunhuan':False,
        'enable links':False,'db_start':100,'db_size':4
        ,'db_end':143,'db_byte-sum':0,'db_cycle-sum':0,'路径':''}
dict_2={'value1':0,'value2':0,'value3':0,}
list1=[0,0,0,0,0,0,0,0,0,0,0]



def bi():

   window_1=tk.Tk()
   window_1.title('snap7读写西门子PLC')
   window_1.geometry('700x400')

   
   
   def ps_set():     #parameter settings  DB设置弹出界面
      db_set=tk.Toplevel()
      db_set.minsize(width=300,height=300)
      db_set.title('DB设置')
    
   def change_state():
      dict_1['Ipaddress']=V1.get()# 调用get()方法，将Entry中的内容获取出来
      dict_1['db_start']=int(V2.get())
      dict_1['db_end']=int(V3.get())
      dict_1['db_size']=int(V4.get())
      print(dict_1['Ipaddress'])
      print(dict_1['db_start'])
      print(dict_1['db_end'])
      print(dict_1['db_size'])

   def bool_set1():
       dict_1['enable links']=True
       

   def flushes_1():
       read.ri()
           
       var100.set(list1[0])
       var101.set(list1[1])
       var102.set(list1[2])
       var103.set(list1[3])
       var104.set(list1[4])
       var105.set(list1[5])
       var106.set(list1[6])
       var107.set(list1[7])
       var108.set(list1[8])
       var109.set(list1[9])
       var110.set(list1[10])
       window_1.after(2000,flushes_1)

   def slecpath():
         #path_=tkinter.filedialog.askopenfilename() #选择文件
         path_=tkinter.filedialog.askdirectory()#选择路径
         print(path_)
         path_=path_.replace("/","\\\\")
         dict_1['路径']=path_
         var111.set(path_) 

   var1 = tk.StringVar()
   V1 = tk.Entry(window_1,width=15,textvariable=var1)#输入窗口
   V1.place(x = 40,y = 10,anchor='nw')
   var1.set(dict_1['Ipaddress'])

   var2 = tk.StringVar()
   V2 = tk.Entry(window_1,width=4,textvariable=var2)#起始输入窗口
   V2.place(x = 175,y = 10,anchor='nw')
   var2.set(dict_1['db_start'])

   var3 = tk.StringVar()
   V3 = tk.Entry(window_1,width=4,textvariable=var3)#结束输入窗口
   V3.place(x = 260,y = 10,anchor='nw')
   var3.set(dict_1['db_end'])

   var4 = tk.StringVar()
   V4 = tk.Entry(window_1,width=4,textvariable=var4)#数据宽度输入窗口
   V4.place(x = 360,y = 10,anchor='nw')
   var4.set(dict_1['db_size'])

   label_1=tk.Label(window_1,text='IP地址',width=5,height=1,anchor='w',justify='right')#row行，colum列
   label_1.place(x = 1,y = 10,anchor='nw')

   label_2=tk.Label(window_1,text='湿度',width=5,height=1,anchor='w',justify='right')#row行，colum列
   label_2.place(x = 1,y = 60,anchor='nw')

   label_3=tk.Label(window_1,text='温度',width=5,height=1,anchor='w',justify='right')#row行，colum列
   label_3.place(x = 1,y = 100,anchor='nw')

   label_4=tk.Label(window_1,text='CO2浓度1',width=8,height=1,anchor='w',justify='right')#row行，colum列
   label_4.place(x = 80,y = 60,anchor='nw')

   label_5=tk.Label(window_1,text='CO2浓度2',width=8,height=1,anchor='w',justify='right')#row行，colum列
   label_5.place(x = 80,y = 100,anchor='nw')

   label_6=tk.Label(window_1,text='起始地址',width=7,height=1,anchor='w',justify='right')#row行，colum列
   label_6.place(x = 120,y = 10,anchor='nw')
   
   label_7=tk.Label(window_1,text='结束地址',width=7,height=1,anchor='w',justify='right')#row行，colum列
   label_7.place(x = 200,y = 10,anchor='nw')

   label_8=tk.Label(window_1,text='PM2.5',width=8,height=1,anchor='w',justify='right')#row行，colum列
   label_8.place(x = 190,y = 60,anchor='nw')

   label_9=tk.Label(window_1,text='PM10',width=8,height=1,anchor='w',justify='right')#row行，colum列
   label_9.place(x = 190,y = 100,anchor='nw')

   label_10=tk.Label(window_1,text='N2瞬时流量',width=10,height=1,anchor='w',justify='right')#row行，colum列
   label_10.place(x = 280,y = 60,anchor='nw')

   label_11=tk.Label(window_1,text='CO2瞬时流量',width=10,height=1,anchor='w',justify='right')#row行，colum列
   label_11.place(x = 400,y = 60,anchor='nw')

   label_12=tk.Label(window_1,text='N2累计流量',width=10,height=1,anchor='w',justify='right')#row行，colum列
   label_12.place(x = 280,y = 100,anchor='nw')

   label_13=tk.Label(window_1,text='CO2累计流量',width=10,height=1,anchor='w',justify='right')#row行，colum列
   label_13.place(x = 400,y = 100,anchor='nw')

   label_14=tk.Label(window_1,text='风机计数',width=10,height=1,anchor='w',justify='right')#row行，colum列
   label_14.place(x = 520,y = 60,anchor='nw')

   label_15=tk.Label(window_1,text='数据宽度',width=7,height=1,anchor='w',justify='right')#row行，colum列
   label_15.place(x = 300,y = 10,anchor='nw')

   var100 = tk.StringVar()#湿度
   label_100=tk.Label(window_1,textvariable=var100,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_100.place(x = 35,y = 60,anchor='nw')

   
   var101 = tk.StringVar()#温度
   label_101=tk.Label(window_1,textvariable=var101,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_101.place(x = 35,y = 100,anchor='nw')

   var102 = tk.StringVar()#CO2浓度1
   label_102=tk.Label(window_1,textvariable=var102,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_102.place(x = 150,y = 60,anchor='nw')

   var103 = tk.StringVar()#CO2浓度2
   label_103=tk.Label(window_1,textvariable=var103,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_103.place(x = 150,y = 100,anchor='nw')

   var104 = tk.StringVar()#PM2.5
   label_104=tk.Label(window_1,textvariable=var104,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_104.place(x = 235,y = 60,anchor='nw')

   var105 = tk.StringVar()#PM10
   label_105=tk.Label(window_1,textvariable=var105,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_105.place(x = 235,y = 100,anchor='nw')

   var106 = tk.StringVar()#N2瞬时流量
   label_106=tk.Label(window_1,textvariable=var106,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_106.place(x = 350,y = 60,anchor='nw')

   var107 = tk.StringVar()#CO2瞬时流量
   label_107=tk.Label(window_1,textvariable=var107,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_107.place(x = 480,y = 60,anchor='nw')

   var108 = tk.StringVar()#N2累计流量
   label_108=tk.Label(window_1,textvariable=var108,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_108.place(x = 350,y = 100,anchor='nw')

   var109 = tk.StringVar()#CO2累计流量
   label_109=tk.Label(window_1,textvariable=var109,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_109.place(x = 480,y = 100,anchor='nw')

   var110 = tk.StringVar()#风机计数
   label_110=tk.Label(window_1,textvariable=var110,width=5,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_110.place(x = 580,y = 60,anchor='nw')

   var111 = tk.StringVar()#文件路径
   label_111=tk.Label(window_1,textvariable=var111,width=20,height=1,bg='white',anchor='w',justify='right')#row行，colum列
   label_111.place(x = 35,y = 200,anchor='nw')

   button1= tk.Button(window_1,text='单击',height=1,width=5,command=change_state)
   button1.place(x = 450,y = 5,anchor='nw')

   #Button2=tk.Button(window_1, text='DB设置', command=ps_set)
   #Button2.place(x = 300,y = 5,anchor='nw')

   Button3=tk.Button(window_1, text='开始循环', command=bool_set1)
   Button3.place(x = 600,y = 5,anchor='nw')

   Button4=tk.Button(window_1, text='选择文件保存路径', command=slecpath)
   Button4.place(x = 300,y = 200,anchor='nw')

   window_1.after(2000,flushes_1)

   window_1.mainloop()
       
    
   
import tkinter as tk
from tkinter import*
import  pandas
import tkinter.filedialog
import os
import xlrd
import numpy
import openpyxl
#D:/工作/氢氧化锂/程序+触摸屏/信息表.xls

wb=openpyxl.load_workbook('D:/工作/氢氧化锂/程序+触摸屏/信息表.xlsx')
ws = wb.active
#ws.title='test'
ws.cell(row=2,column=2,value=4)
wb.save('D:/工作/氢氧化锂/程序+触摸屏/信息表.xlsx')
#data1 = pandas.read_excel('D:/工作/氢氧化锂/程序+触摸屏/信息表.xlsx')
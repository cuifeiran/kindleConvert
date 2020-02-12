#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/12 22:04
# @Author   : CuiFeiran
# @FileName : kindleConvert.py
# @Software : PyCharm
# @email    :cui2025@126.com
# @Blog     : https://blog.csdn.net/qq_33273956
# @bilibili : https://space.bilibili.com/368768799


from bs4 import BeautifulSoup
from tkinter.filedialog import *
import tkinter.messagebox

def select_path_in():
    global path_in
    path_in = askopenfilename()
    lb_in.config(text='文件路径' + path_in)

def select_path_out():
    global path_out
    path_out=askdirectory()
    lb_out.config(text='输出路径' + path_out)
def convert():
    # path = '/Users/cui/Downloads/Notebook.html'  # 设置书签路径
    html = open(path_in, 'r', encoding='utf-8').read()
    bs = BeautifulSoup(html, "html.parser")
    booktitle = bs.find_all(class_='bookTitle')[0].get_text().strip()  # 获取书名--noteHeading
    authors = bs.find_all(class_='authors')[0].get_text().strip()  # 获取作者名--authors
    noteheading = bs.find_all(class_='noteHeading')  # 获取标注时间和位置--noteHeading
    notetext = bs.find_all(class_='noteText')  # 获取标注内容--noteText
    notetext_num = len(notetext)  # 获取书签的条数
    noteheading_num = 0
    f = open(path_out+'/My Clippings.txt', 'w', encoding='utf8')
    for i in range(notetext_num):
        if '书签' in noteheading[i]:
            f.write(booktitle + authors + '\n')  # 图书信息
            f.write(noteheading[i].get_text())  # 图书标注位置
            f.write('这是一条书签\n')  # 图书标注内容为书签
            f.write('==========' + '\n')
            noteheading_num = noteheading_num + 1
        else:
            f.write(booktitle + authors + '\n')  # 图书信息
            f.write('- ' + noteheading[noteheading_num].get_text().lstrip() + '\n')  # 图书标注位置
            f.write(notetext[i].get_text() + '\n')  # 图书标注内容
            f.write('==========' + '\n')  # 结束
            noteheading_num = noteheading_num + 1
            i = i + 1
    f.close()
    tkinter.messagebox.showinfo('转换完成','转换完成！文件文件保存在:'+path_out)

root = Tk()
root.geometry('500x200')
root.title('Kindle的html笔记转txt工具')


lb_in=Label(root, text='')
lb_in.grid(row=0, column=1)
Button(root, text="选择Html文件", command=select_path_in).grid(row=0, column=2)

lb_out=Label(root, text='')
lb_out.grid(row=1, column=1)
Button(root, text="选择输出路径", command=select_path_out).grid(row=1, column=2)
Button(root, text="转换", command=convert).grid(columnspan=2,sticky=W)
root.mainloop()
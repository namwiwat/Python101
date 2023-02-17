from tkinter import *
from tkinter import ttk
from tkinter import messagebox
GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')
L1 = Label(GUI,text='โปร
L1.place(x=30,y20)

###################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 10 บาท'
    messagebox.showinfo('เงินในบช',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
###################################

def Button3():
    text = 'Python 101'
    messagebox.showinfo('เรียนวันที่ 10-20',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=100)
B3 = ttk.Button(FB2,text='สัปดาเรียนวิชา',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()

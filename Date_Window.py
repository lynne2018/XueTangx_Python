from tkinter import *
import tkinter
import tkinter.messagebox

#判断是否为闰年：年份能被四整除并能不被100整除或者能被400整除
def isLeapYear(nYear):
    if ((nYear%4==0) and (nYear%100!=0)) or (nYear%400==0):
        return 1
    else:
        return 0

def totalDays(nYear,nMonth,nDay):
    i=1
    nSumDays = 0
    #遍历到输入月份之前的月，确定每个月的天数
    while i<nMonth:
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            nMonthDays = 31
        elif i==4 or i==6 or i==9 or i==11:
            nMonthDays = 30
        elif i==2:
            if isLeapYear(nYear) == 1:
                nMonthDays = 29
            elif isLeapYear(nYear) == 0:
                nMonthDays = 28
        #获取输入月份之前月份的总天数

        nSumDays = nSumDays + nMonthDays
        i = i+1
    #计算总天数：输入月份之前月份的总天数加上输入的日期
    nSumDays = nSumDays + nDay
    return nSumDays

            

root = Tk()
root.minsize(370,210)
root.title('日期计算器')

label_title = Label(root,text="请输入日期，计算从元旦到改日期的天数: ",font=('宋体',15))
label_title.place(x=30,y=20)

text_year = Entry(root,width=6)
text_year.place(x=60,y=70)

label_year = Label(root,text="年",font=('宋体',15))
label_year.place(x=120,y=70)

text_month = Entry(root,width=6)
text_month.place(x=150,y=70)

label_month = Label(root,text="月",font=('宋体',15))
label_month.place(x=210,y=70)

text_day = Entry(root,width=6)
text_day.place(x=240,y=70)

label_day = Label(root,text="日",font=('宋体',15))
label_day.place(x=300,y=70)

def btn_Cal():
    nYear_text = text_year.get()
    nMonth_text = text_month.get()
    nDay_text = text_day.get()
    if nYear_text=='' or nMonth_text=='' or nDay_text=='':
        msg_text.set('')
        date_text.set('')
        tkinter.messagebox.showinfo("提示","请重新填写")
    else:
        nYear = int(nYear_text)
        nMonth = int(nMonth_text)
        nDay = int(nDay_text)
        if nMonth < 1 or nMonth >12:
            #print("请输入正确的月份：1-12")
            tkinter.messagebox.showinfo("提示","请输入正确的月份：1-12")
            text_month.delete(0,END)
            return None
        if (nDay < 0 or nDay >31) and (nMonth==1 or nMonth==3 or nMonth==5 or nMonth==7 or nMonth==8 or nMonth==10 or nMonth==12):
            #print("请输入正确的日期：1-31")
            tkinter.messagebox.showinfo("提示","请输入正确的日期：1-31")
            text_day.delete(0,END)
            return None
        elif (nDay < 0 or nDay >30) and (nMonth==4 or nMonth==6 or nMonth==9 or nMonth==11):
            #print("请输入正确的日期：1-30")
            tkinter.messagebox.showinfo("提示","请输入正确的日期：1-30")
            text_day.delete(0,END)
            return None
        elif (nDay < 0 or nDay >29) and (isLeapYear(nYear)==1) and nMonth==2:
            #print("请输入正确的日期：1-29")
            tkinter.messagebox.showinfo("提示","请输入正确的日期：1-29")
            text_day.delete(0,END)
            return None
        elif (nDay < 0 or nDay >28) and (isLeapYear(nYear)==0) and nMonth==2:
            #print("请输入正确的月份：1-28")
            tkinter.messagebox.showinfo("提示","请输入正确的日期：1-28")
            text_day.delete(0,END)
            return None
        else:
            nSumDays = totalDays(nYear,nMonth,nDay)
            msg_text.set("总天数为：")
            date_text.set(nSumDays)

def btn_Clr():
    text_year.delete(0,END)
    text_month.delete(0,END)
    text_day.delete(0,END)
    msg_text.set('')
    date_text.set('')
    text_year.focus()   

btlCal = Button(root,text="计算",command=btn_Cal)
btlCal.place(x=80,y=120,width=80)
btlClr = Button(root,text="重置",command=btn_Clr)
btlClr.place(x=200,y=120,width=80)

msg_text = StringVar()
date_text = StringVar()

label_msg = Label(root,textvariable=msg_text,font=('宋体',20))
label_msg.place(x=100,y=170,height=25)
label_sumDay = Label(root,textvariable=date_text,font=('宋体',15),fg='red')
label_sumDay.place(x=200,y=170,height=25)


root.mainloop()
    
    
    

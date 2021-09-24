from tkinter import *
from datetime import datetime
app=Tk()
app.geometry('600x200')
app.title("Age Calculator")
msg=Label(app,text="Your D.O.B",background="black",foreground="red", font=("Times",20))
msg.grid(row=0,column=0,padx=25,pady=5,columnspan=6)
app['background']="black"
day=Label(app,text="Day: ",background="black",foreground="yellow")
dayE=Entry(app,width=7,background="grey",foreground="black")

month=Label(app,text=" Month: ",background="black",foreground="yellow")
monthE=Entry(app,width=7,background="grey",foreground="black")

year=Label(app,text=" Year: ",background="black",foreground="yellow")
yearE=Entry(app,width=10,background="grey",foreground="black")

day.grid(row=1,column=0,padx=25,pady=5)
dayE.grid(row=1,column=1,padx=25,pady=5)
month.grid(row=1,column=2,padx=25,pady=5)
monthE.grid(row=1,column=3,padx=25,pady=5)
year.grid(row=1,column=4,padx=25,pady=5)
yearE.grid(row=1,column=5,padx=25,pady=5,)

def total_days():
    dat=int(dayE.get())
    mon=int(monthE.get())
    yer=int(yearE.get())
    dob=datetime(day=dat,month=mon,year=yer)
    now=datetime.now()
    timediff=now-dob
    dy=Label(app,font=('Times',15),text="You have lived "+ str(timediff.days)+" days!",background="black",foreground="cyan")
    dy.grid(row=3,column=0,padx=25,pady=5,columnspan=6)

def total_sec():
    dat = int(dayE.get())
    mon = int(monthE.get())
    yer = int(yearE.get())
    dob = datetime(day=dat, month=mon, year=yer)
    now = datetime.now()
    timediff = now - dob
    sec = Label(app,font=('Times',15), text="You have lived " + str(timediff.total_seconds()) + " Seconds!",background="black",foreground="cyan")
    sec.grid(row=4, column=0, padx=25, pady=5,columnspan=6)


B=Button(app,text="Days Lived",command=total_days,background='grey')
B.grid(row=2,column=1,padx=25,pady=5,columnspan=2)
C=Button(app,text="Seconds Lived",command=total_sec,background='grey')
C.grid(row=2,column=3,padx=25,pady=5,columnspan=2)

app.mainloop()
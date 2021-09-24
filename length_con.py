from tkinter import *

app=Tk()
app.title("Length Convertor")
scales=['Meters','Inches','Feet']
option=StringVar()
menu=OptionMenu(app,option,*scales)
menu.grid(row=0,column=0,padx=25,pady=10)
lbl=Label(app,text="Convert to")
lbl.grid(row=0,column=1,padx=25,pady=10)
option1=StringVar()
menu=OptionMenu(app,option1,*scales)
menu.grid(row=0,column=2,padx=25,pady=10)
enterL=Entry(app)
enterL.grid(row=1,column=0,padx=25,pady=10)

def convertor():
    fro=option.get()
    to=option1.get()
    num=float(enterL.get())
    if fro=='Meters' and to=='Inches':
        conv=num*39.37
    elif fro=='Meters' and to=='Foot':
        conv=num*3.28
    elif fro=='Inches' and to=='Meters':
        conv=num/39.37
    elif fro=='Inches' and to=='Foot':
        conv=num*12
    elif fro=='Foot' and to=='Meters':
        conv=num/3.28
    elif fro=='Foot' and to=='Inches':
        conv=num*12
    else:
        conv=num
    lb=Label(app,text=round(conv,2))
    lb.grid(row=1, column=1, padx=25, pady=10)

B=Button(app,text="Convert",command=convertor)
B.grid(row=2, column=1,columnspan=2, padx=25, pady=10)
app.mainloop()
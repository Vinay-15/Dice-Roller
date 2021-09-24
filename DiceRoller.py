from tkinter import *
app=Tk()
app.title("Dice Roller")
app["background"]="black"
Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}
die=Label(app, text=Dice[0], font=('Times',100), background='black',foreground="red")
die.grid(row=0,column=0,padx=25,pady=5)

def roll():
    from random import randint
    i=randint(1,6)
    lbl=Label(app, text=Dice[i], font=('Times',100), background='black',foreground="red", width=2)
    lbl.grid(row=0, column=0, padx=25, pady=5)

B=Button(app, text="Roll", command=roll, background='grey')
B.grid(row=1,column=0,padx=25, pady=5)
app.mainloop()
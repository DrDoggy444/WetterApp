from  tkinter import *
from tkinter import ttk
#Window Setup
MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
#screenReso = str(MAINWINDOW.winfo_screenwidth()) + 'x' + str(MAINWINDOW.winfo_screenheight())
screenReso = '800x600'
MAINWINDOW.geometry(screenReso)

##TextfelderSetup
CityInputtext = Text(MAINWINDOW,height=1, width=10)
CityInputtext.place(x=350, y= 200)


##ButtonSetup
def okOnClick(*args, method): #OnKlick-Event für main
    method(args)
ok = ttk.Button(MAINWINDOW, text='ok',command=okOnClick)
ok.place(x= 500, y= 500)


MAINWINDOW.mainloop()

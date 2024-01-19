from  tkinter import *
from tkinter import ttk
#Window Setup
MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
screenReso = str(MAINWINDOW.winfo_screenwidth()) + 'x' + str(MAINWINDOW.winfo_screenheight())
MAINWINDOW.geometry(screenReso)

##TextfelderSetup
CityInputtext = Text(MAINWINDOW,height=1, width=10)
CityInputtext.place(x=MAINWINDOW.winfo_screenwidth()/2, y=MAINWINDOW.winfo_screenheight()/4)


##ButtonSetup
ok = ttk.Button(MAINWINDOW, text='ok')
ok.place(x= 500, y= 500)

MAINWINDOW.mainloop()

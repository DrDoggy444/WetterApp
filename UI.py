from  tkinter import *
from tkinter import ttk
import API_calls
#Window Setup
MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
#screenReso = str(MAINWINDOW.winfo_screenwidth()) + 'x' + str(MAINWINDOW.winfo_screenheight())
screenReso = '800x600'
MAINWINDOW.geometry(screenReso)

##TextfelderSetup
CityInputtext = Text(MAINWINDOW,height=1, width=10)
CityInputtext.place(x=350, y= 200)

def getInput():
    CityInputtext.get(1.0, END)
##ButtonSetup
def okOnClick(): #OnKlick-Event für main
    print(API_calls.call.getCurrentWeather(getInput()))
ok = ttk.Button(MAINWINDOW, text='ok',command=okOnClick)
ok.place(x= 500, y= 500)


MAINWINDOW.mainloop()

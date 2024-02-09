from  tkinter import *
from tkinter import ttk
import API_calls
#Window Setup
MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
#screenReso = str(MAINWINDOW.winfo_screenwidth()) + 'x' + str(MAINWINDOW.winfo_screenheight())
screenReso = '800x400'
MAINWINDOW.geometry(screenReso)

##TextfelderSetup
CityInputtext = Text(MAINWINDOW,height=1, width=20)
CityInputtext.place(x=150, y= 100)


    
##ButtonSetup
def okOnClick(): #OnKlick-Event für main
    Inputcity =  CityInputtext.get(1.0, END)
    print(API_calls.call.getCurrentWeather(city= Inputcity))
ok = ttk.Button(MAINWINDOW, text='ok',command=okOnClick)
ok.place(x= 350, y= 99)


#customShapes

IsOnline = Canvas(MAINWINDOW,height=50,width=40)
IsOnline.grid()
IsOnline.create_oval(1,1,40,40,fill='green',state='disabled')


MAINWINDOW.mainloop()

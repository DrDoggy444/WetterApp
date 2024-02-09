from  tkinter import *
from tkinter import ttk
from API_calls import WeatherAPI

#Window Setup
MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
#screenReso = str(MAINWINDOW.winfo_screenwidth()) + 'x' + str(MAINWINDOW.winfo_screenheight())
screenReso = '600x300'
MAINWINDOW.geometry(screenReso)

##TextfelderSetup
CityInputtext = Text(MAINWINDOW,height=1, width=20)
CityInputtext.place(x=150, y= 100)


    
##ButtonSetup
def okOnClick(): #OnKlick-Event für main
    Inputcity =  CityInputtext.get(1.0, END)
    isOnline()
    print(WeatherAPI.getCurrentWeather(city= Inputcity))
ok = ttk.Button(MAINWINDOW, text='ok',command=okOnClick)
ok.place(x= 350, y= 99)


#OnlineCheckVisual

IsOnline = Canvas(MAINWINDOW,height=50,width=40)
IsOnline.grid()
NoConnection = ttk.Label(MAINWINDOW)
NoConnection.place(x=15,y=50)   
def isOnline():
    if WeatherAPI.CheckOnlineStatus():
        IsOnline.create_oval(10,10,40,40,fill='green',state='disabled')
        NoConnection.config(text='')
    else: #keine Verbindung da
        IsOnline.create_oval(10,10,40,40,fill='red',state='disabled')
        NoConnection.config(text='Es konnte keine Verbindung zum Service aufgebaut werden.\nBitte das Programm neustarten')




#TreeviewSetup

resultTable = ttk.Treeview(MAINWINDOW)
resultTable.place(x=1, y=150,height=150,width=600)

resultTable['columns'] = ('Temperatur')
resultTable.column('Temperatur', width= 10)
resultTable.heading('Temperatur', text='Temperatur')



#Runtime
isOnline()
MAINWINDOW.resizable(0,0)
MAINWINDOW.mainloop()

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
CityInputtext.place(x=220, y= 100)


    
##ButtonSetup
def ButtonOnClick(): #OnKlick-Event für main
    if isOnline():
        Inputcity =  CityInputtext.get(1.0, END)
        celsius =  WeatherAPI.getCurrentWeather(city= Inputcity)
        resultTable.insert('', END, values=( Inputcity, celsius))
ok = ttk.Button(MAINWINDOW, text='Abfragen',command=ButtonOnClick)
ok.place(x= 400, y= 99)


#OnlineCheckVisual

IsOnline = Canvas(MAINWINDOW,height=50,width=40)
IsOnline.grid()
NoConnection = ttk.Label(MAINWINDOW)
NoConnection.place(x=15,y=50)   
def isOnline() -> bool:
    if WeatherAPI.CheckOnlineStatus():
        IsOnline.create_oval(10,10,40,40,fill='green',state='disabled')
        NoConnection.config(text='')
        return True
    else: #keine Verbindung da
        IsOnline.create_oval(10,10,40,40,fill='red',state='disabled')
        NoConnection.config(text='Es konnte keine Verbindung zum Service aufgebaut werden.\nBitte das Programm neustarten')
        return False




#TreeviewSetup

resultTable = ttk.Treeview(MAINWINDOW)
resultTable.place(x=1, y=150,height=150,width=600)
resultTable.column("#0", width = 0, stretch = "no") #Kinderkrankheit beseitigen(Leeres Spalte weg)
#Stadt
resultTable['columns'] = ('Stadt','Temperatur')
resultTable.column('Stadt', width= 300, stretch= False)
resultTable.heading('Stadt', text='Stadt',anchor=W)
#Temp
resultTable.column('Temperatur', width= 300, stretch= False)
resultTable.heading('Temperatur', text='Temperatur',anchor=W)
#Scrollbar
scrollbar = ttk.Scrollbar(resultTable, orient="vertical", command=resultTable.yview)
scrollbar.pack(side='right', fill='y')
resultTable.configure(yscrollcommand=scrollbar.set)

#Runtime
isOnline()
MAINWINDOW.resizable(0,0)
MAINWINDOW.mainloop()

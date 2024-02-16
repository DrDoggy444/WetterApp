from  tkinter import *
from tkinter import ttk 
from API_calls import WeatherAPI


##Window Setup
MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
screenReso = '600x300'
MAINWINDOW.geometry(screenReso)
MAINWINDOW.iconbitmap('./Ressources/WeatherApp.ico')

##TextfelderSetup
CityInputtext = Text(MAINWINDOW,height=1, width=20)
CityInputtext.place(x=220, y= 100)

##LabelSetup
NoConnection = ttk.Label(MAINWINDOW)
NoConnection.place(x=15,y=50) 

inValidRequest = ttk.Label(MAINWINDOW)
inValidRequest.place(x=220, y= 70)


##ButtonSetup
def ButtonOnClick(): #OnKlick-Event für main
    if isOnline():
        Inputcity =  CityInputtext.get(1.0, END)
        celsius =  WeatherAPI.getTemperatur(Inputcity)
        windSpeed = WeatherAPI.getWindSpeeds(Inputcity)
        if WeatherAPI.validRequest(celsius):
            inValidRequest.config(text='')
            resultTable.insert('', 0, values=( Inputcity, celsius, windSpeed))
        else:
            inValidRequest.config(text='Für die angefragte Stadt existieren keine Wetterdaten!')
ok = ttk.Button(MAINWINDOW, text='Abfragen',command=ButtonOnClick)
ok.place(x= 400, y= 99)

##KeyboardEvents
def onKeyPress(event): 
    if event.char == '\r': #"Enter" abfangen
       ButtonOnClick()
       CityInputtext.delete('1.0',END)
MAINWINDOW.bind('<KeyPress>',onKeyPress)


##OnlineCheckVisual

IsOnline = Canvas(MAINWINDOW,height=50,width=40)
IsOnline.place(x=0, y=0)
def isOnline() -> bool:
    if WeatherAPI.CheckOnlineStatus():
        IsOnline.create_oval(10,10,40,40,fill='green',state='disabled')
        NoConnection.config(text='')
        return True
    else: #keine Verbindung da
        IsOnline.create_oval(10,10,40,40,fill='red',state='disabled')
        NoConnection.config(text='Es konnte keine Verbindung zum Service aufgebaut werden.\nBitte versuchen Sie es später erneut')
        return False




##TreeviewSetup

resultTable = ttk.Treeview(MAINWINDOW)

resultTable.place(x=1, y=130,height=180,width=600)
resultTable.column("#0", width = 0, stretch = "no",) #"Kinderkrankheit" beseitigen(Leere Spalte am Anfang weg)
#Stadt
resultTable['columns'] = ('Stadt','Temperatur','Wind','Bild')
resultTable.column('Stadt', width= 250, stretch= False)
resultTable.heading('Stadt', text='Stadt',anchor=W)
#Temp
resultTable.column('Temperatur', width= 100, stretch= False)
resultTable.heading('Temperatur', text='Temperatur',anchor=W)
#Wind
resultTable.column('Wind', width= 300, stretch= False)
resultTable.heading('Wind', text='Wind',anchor=W)

#Scrollbar
scrollbar = ttk.Scrollbar(resultTable, orient="vertical", command=resultTable.yview)
scrollbar.pack(side='right', fill='y')
resultTable.configure(yscrollcommand=scrollbar.set)


##Runtime
##Alle Konfigurationen für Events MÜSSEN vor .mainloop() passieren, da .mainloop() eine Dauerschleife bis Programmende ist
isOnline()
MAINWINDOW.resizable(0,0)
MAINWINDOW.mainloop()

from  tkinter import *
from tkinter import ttk

MAINWINDOW = Tk(screenName= 'mainWindow',className='WetterApp')
screenReso = str(MAINWINDOW.winfo_screenwidth()) + 'x' + str(MAINWINDOW.winfo_screenheight())
MAINWINDOW.geometry(screenReso)


frame = ttk.Frame(MAINWINDOW, width=1920 , height= 1080)
frame.grid()
ttk.Button(frame, text='test', command=MAINWINDOW.destroy).pack()
ttk.Button(frame, text='test2', command=MAINWINDOW.destroy).grid(column=0, row=1)
MAINWINDOW.mainloop()

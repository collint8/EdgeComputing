import os
import matplotlib
import subprocess
import numpy as np
import tkinter as tk
matplotlib.use('TkAgg')
from tkinter import ttk
from PIL import ImageTk,Image
import agg_main_vF as aggr_main
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
'''
	This is the file for the GUI A lot of it is resizing and repositioning
	abandon hope all ye who enter here.
'''
LARGE_FONT1=('Times',16)
LARGE_FONT=('Times',18,'bold')

class TopMain(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self,'Federated Learning Demonstration')
        tk.Tk.iconbitmap(self,default='PicU.ico')
        
        container=tk.Frame(self)
        container.grid(sticky='n')
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames={}
        for F in (StartPage,Graph):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0, sticky='nsew')
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        def checkDisable():
            if cb.get()==1:
                entry0.config(state='disabled')
                entry1.config(state='disabled')
                #entry2.config(state='disabled')
                #entry3.config(state='disabled')
            elif cb.get()==0:
                entry0.config(state='normal')
                entry1.config(state='normal')
                #entry2.config(state='normal')
                #entry3.config(state='normal')
        def startProgram(host='192.168.5.2',node_ip=['192.168.5.3'],K=2,Tau=5,win= np.zeros(784)):
            if cb.get()== 1:
                aggr_main.run(2,shuff=shuff.get(),avc=avc.get())
            elif k.get()>=1 and tau.get()>=1 and shuff.get()>=0 and avc.get()>=0:
                aggr_main.run(k.get(),tau=tau.get(),shuff=shuff.get(),avc=avc.get())
            else:
                print('Invalid Values')
        tk.Frame.__init__(self,parent)
        welcome1=tk.Label(self,text='Welcome to the University of Utah Computer and Electrical Engineering',font=LARGE_FONT)
        welcome2=tk.Label(self,text='Technical Open House 2019 - Federated Learning Senior Capstone Project',font=LARGE_FONT)
        welcome3=tk.Label(self,text='Thank you for your interest in our project',font=LARGE_FONT)
        welcome4=tk.Label(self,text='    ',font=LARGE_FONT)
#initiate variables
        k = tk.IntVar(self,'2')
        tau = tk.IntVar(self,'5')
        shuff = tk.IntVar(self,'0')
        avc = tk.IntVar(self,'0')

        cb = tk.IntVar()
#link variables with text boxes
        entry0=tk.Entry(self,textvariable=k,font=LARGE_FONT1)
        entry1=tk.Entry(self,textvariable=tau,font=LARGE_FONT1)
        entry2=tk.Entry(self,textvariable=shuff,font=LARGE_FONT1)
        entry3=tk.Entry(self,textvariable=avc,font=LARGE_FONT1)

        button9=ttk.Button(self,text='Start',command=startProgram)

        c=tk.Checkbutton(self,variable=cb,text='Use Default Initial Conditions?',command=checkDisable,font=LARGE_FONT1)

        label0=tk.Label(self,text='Number of Global updates (K)',font=LARGE_FONT1)
        label1=tk.Label(self,text='Number of iterations between each K (\u03c4)',font=LARGE_FONT1)
        label2=tk.Label(self,text='Shuffling type (0-3)',font=LARGE_FONT1)
        label3=tk.Label(self,text='Processing style (0-2)',font=LARGE_FONT1)

		# label2=tk.Label(self,text='Tradeoff control parameter (\u03bb)',font=LARGE_FONT1)
        # label3=tk.Label(self,text='Initial step size (\u03f5)',font=LARGE_FONT1)
        
        inst2=tk.Label(self,text='(Default conditions are: \u03bb = 1, K = 2, \u03c4 = 5, & \u03f5 = 0.01)',font=LARGE_FONT1)

        welcome1.grid(row=2,pady=(10,0))
        welcome2.grid(row=3)
        welcome3.grid(row=4,pady=(0,10))
        c.grid(row=5)
        label0.grid(row=7,sticky='w')
        entry0.grid(row=7,sticky='e')
        label1.grid(row=8,sticky='w')
        entry1.grid(row=8,sticky='e')
        label2.grid(row=9,sticky='w')
        entry2.grid(row=9,sticky='e')
        label3.grid(row=10,sticky='w')
        entry3.grid(row=10,sticky='e')

#        button8.pack()fd
        inst2.grid(row=6,pady=(0,10))
        button9.grid(row=14,pady=10)
#        button10.pack()

        path= 'TheBestPictureEver.png'
        pic=ImageTk.PhotoImage(Image.open(path))
        panel=tk.Label(image=pic)
        panel.image=pic
        panel.grid(row=15,sticky='nsew')

class Graph(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text='Graph',font=LARGE_FONT)
#        label.pack(pady=10,padx=10)
        f=Figure()
        a1=f.add_subplot(111)
        a1.plot([1,2,3,4],[1,9,3,5])
        
        canvas=FigureCanvasTkAgg(f,self)
        canvas.draw()
#        canvas.get_tk_widget().pack(side='top',fill='both',expand=True)
        
        toolbar=NavigationToolbar2Tk(canvas,self)
        toolbar.update()
#        canvas._tkcanvas.pack(side='top',fill='both',expand=True)
        
app=TopMain()
app.mainloop()

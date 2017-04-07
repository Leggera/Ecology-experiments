import Tkinter as Tk
from Manager import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.patches as patches

class Application(Tk.Frame):
    def __init__(self, master = None):
        Tk.Frame.__init__(self, master)
        self.master = master
        
        
        self.initialize()

    def initialize(self):
        self.grid()
        self.createWidgets()

        
        
        self.entryVariable1 = Tk.StringVar()
        self.entry1 = Tk.Entry(self, textvariable=self.entryVariable1)
        self.entry1.grid(column=1,row=0,sticky='EW')

        self.labelVariable1 = Tk.StringVar()
        label1 = Tk.Label(self,textvariable=self.labelVariable1,
                              anchor="w",fg="black",bg="yellow")
        label1.grid(column=0,row=0,columnspan=1 ,sticky='EW')
        self.labelVariable1.set( "N" )

        self.entryVariable2 = Tk.StringVar()
        self.entry2 = Tk.Entry(self,textvariable=self.entryVariable2)
        self.entry2.grid(column=1,row=1,sticky='EW')

        self.labelVariable2 = Tk.StringVar()
        label2 = Tk.Label(self,textvariable=self.labelVariable2,
                              anchor="w",fg="black",bg="yellow")
        label2.grid(column=0,row=1,columnspan=1 ,sticky='EW')
        self.labelVariable2.set( "K" )

        self.entryVariable3 = Tk.StringVar()
        self.entry3 = Tk.Entry(self,textvariable=self.entryVariable3)
        self.entry3.grid(column=1,row=2,sticky='EW')

        self.labelVariable3 = Tk.StringVar()
        label3 = Tk.Label(self,textvariable=self.labelVariable3,
                              anchor="w",fg="black",bg="yellow")
        label3.grid(column=0,row=2,columnspan=1 ,sticky='EW')
        self.labelVariable3.set( "Fund" )

        self.entryVariable4 = Tk.StringVar()
        self.entry4 = Tk.Entry(self,textvariable=self.entryVariable4)
        self.entry4.grid(column=1,row=3,sticky='EW')

        self.labelVariable4 = Tk.StringVar()
        label4 = Tk.Label(self,textvariable=self.labelVariable4,
                              anchor="w",fg="black",bg="yellow")
        label4.grid(column=0,row=3,columnspan=1 ,sticky='EW')

        self.entry1.bind("<Return>", self.OnPressEnter)
        self.entry2.bind("<Return>", self.OnPressEnter)
        self.entry3.bind("<Return>", self.OnPressEnter)
        self.entry4.bind("<Return>", self.OnPressEnter)
        
        self.labelVariable = Tk.StringVar()
        label = Tk.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=4,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        #self.resizable(True,False)
        self.update()
        #self.geometry(self.geometry())#TODO

    def createWidgets(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(column=0,row=5)
        
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xticks(())
        self.ax.set_yticks(())
        self.x = np.linspace(0, 100, 100)
        self.y = np.linspace(0, 100, 100).reshape(-1, 1)


    def OnPressEnter(self,event):
        n1 = self.entryVariable1.get()
        n2 = self.entryVariable2.get()
        n3 = self.entryVariable3.get()
        n4 = self.entryVariable4.get()
        if (n1 == '') or (n2 == '') or (n3 == '') or (n4 == ''):
            self.labelVariable.set("You need to enter every value")
            return
        self.manager = Manager(int(n1), int(n2), int(n3))
        for i in range(250):
            self.manager.main()
            if (i == 0):
                im = self.ax.imshow(f(self.x, self.y, self.manager.Town.Companies), cmap='YlOrRd', vmin = 0, vmax = 100000, animated=False)#TODO
                for company in self.manager.Town.Companies:
                    x, y = company.location
                    size = company.size
                    self.ax.add_patch(
                    patches.Rectangle(
                        (x, y),   # (x,y)
                        size/2,          # width
                        size/2,          # height
                        hatch='\\',
                        fill=False
                    ))
            else:
                im.set_array(f(self.x, self.y, self.manager.Town.Companies))
            self.canvas.draw()
        #self.entry1.focus_set()#TODO ???
        #self.entry1.selection_range(0, Tk.END)#TODO ???

def f(x, y, Companies):
    poll = np.zeros((len(x), len(y)))
    for company in Companies:
        c1, c2 = company.location
        s = company.size
        c1 += s/4
        c2 += s/4
        poll += company.made_pollution/((x-c1)*(x-c1) + (y-c2)*(y-c2))#TODO devision by zero
    return poll

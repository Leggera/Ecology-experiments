import Tkinter as Tk
from Manager import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.patches as patches
import tkMessageBox
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
        for i in range(25):
            
            Control = Control_data(self)
            self.master.wait_window(Control.top)
            self.manager.main()
            if (i == 0):
                im = self.ax.imshow(f(self.x, self.y, self.manager.Town.Companies), cmap='YlOrRd', vmin = 25000, vmax = 500000, animated=False)#TODO
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
            
            
            #self.stop()
            #self.master.after(1000, self.scanning())
            
        #self.entry1.focus_set()#TODO ???
        #self.entry1.selection_range(0, Tk.END)#TODO ???


class Control_data(Tk.Frame): 
    def __init__(self, master = None):
        self.top = Tk.Toplevel(master)
        self.master= master
        #Tk.Label(top, text="Value").pack()
        self.initialize()

    def OnButtonClick(self):
        Companies = self.master.manager.Town.Companies
        for company in Companies:
            name = company.name
            for i in ["filters", "stop working"]:
                name_i = name+i
                if name_i not in self.master.manager.smth:   
                    self.master.manager.smth[name_i] = 0
        if ('spec.mode' not in self.master.manager.smth):
            self.master.manager.smth['spec.mode'] = 1
        self.top.destroy()
        
    def initialize(self):
        #self.grid()
        self.top.grid()
        
        self.make_entries()
    def make_entries(self):
        self.entry_controlVariable = dict()
        self.entry_control = dict()
        self.label_control = dict()
        self.create_fields("spec.mode", "special mode", 0, 1, 0)
        name_row = 1
        Companies = self.master.manager.Town.Companies
        for company in Companies:
            name = company.name
            name_column = 0
            
            self.label_control[name] = Tk.Label(self.top, text = name )
            self.label_control[name].grid(column=name_column,row=name_row, columnspan = 2)
            i_row = name_row
            self.master.manager.smth[name+"filters"] = 0
            for i in ["filters", "stop working"]:
                
                l_column = 0
                e_column = 1
                i_row = i_row + 1
                self.create_fields(name+i, i, l_column, e_column, i_row)
            name_row += 3
        
        self.button_control = Tk.Button(self.top, text = "OK", command = self.OnButtonClick)
        self.button_control.grid(column = 0, row = name_row+3, columnspan = 2)

    def create_fields(self, s, i, l_c, e_c, i_r):
        self.label_control[s] = Tk.Label(self.top, text = i )
        self.label_control[s].grid(column = l_c, row = i_r) 
        self.entry_control[s] = Tk.Button(self.top, text='Yes', command = lambda: self.YesButton(s))
        self.entry_control[s].grid(column = e_c, row = i_r)
        self.entry_control[s] = Tk.Button(self.top, text='No', command = lambda: self.NoButton(s))
        self.entry_control[s].grid(column = e_c + 1, row = i_r)

    def YesButton(self, name):
        self.master.manager.smth[name] = 1
    def NoButton(self, name):
        self.master.manager.smth[name] = 0
    '''def create_fields(self, s, i, l_c, e_c, i_r):
        self.label_control[s] = Tk.Label(self.top, text = i )
        self.label_control[s].grid(column = l_c, row = i_r) 
        self.entry_controlVariable[s] = Tk.StringVar()       
        self.entry_control[s] = Tk.Entry(self.top, textvariable=self.entry_controlVariable[s])
        self.entry_control[s].grid(column = e_c, row = i_r)'''
                
        
def f(x, y, Companies):
    poll = np.zeros((len(x), len(y)))
    for company in Companies:
        c1, c2 = company.location
        s = company.size
        c1 += s/4
        c2 += s/4
        poll += 1000000 * company.made_pollution/((x-c1)*(x-c1) + (y-c2)*(y-c2))#TODO devision by zero
    return poll


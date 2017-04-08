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
        self.labelVariable1.set( "Car_pollution" )

        self.entryVariable2 = Tk.StringVar()
        self.entry2 = Tk.Entry(self,textvariable=self.entryVariable2)
        self.entry2.grid(column=1,row=1,sticky='EW')

        self.labelVariable2 = Tk.StringVar()
        label2 = Tk.Label(self,textvariable=self.labelVariable2,
                              anchor="w",fg="black",bg="yellow")
        label2.grid(column=0,row=1,columnspan=1 ,sticky='EW')
        self.labelVariable2.set( "Car amount" )

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
        self.labelVariable4.set( "filter_cost")

        self.entryVariable5 = Tk.StringVar()
        self.entry5 = Tk.Entry(self,textvariable=self.entryVariable5)
        self.entry5.grid(column=1,row=4,sticky='EW')

        self.labelVariable5 = Tk.StringVar()
        label5 = Tk.Label(self,textvariable=self.labelVariable5,
                              anchor="w",fg="black",bg="yellow")
        label5.grid(column=0,row=4,columnspan=1 ,sticky='EW')
        self.labelVariable5.set( "fee")

        self.entryVariable6 = Tk.StringVar()
        self.entry6 = Tk.Entry(self,textvariable=self.entryVariable6)
        self.entry6.grid(column=1,row=5,sticky='EW')

        self.labelVariable6 = Tk.StringVar()
        label6 = Tk.Label(self,textvariable=self.labelVariable6,
                              anchor="w",fg="black",bg="yellow")
        label6.grid(column=0,row=5,columnspan=1 ,sticky='EW')
        self.labelVariable6.set( "critical pollution")


        self.entry1.bind("<Return>", self.OnPressEnter)
        self.entry2.bind("<Return>", self.OnPressEnter)
        self.entry3.bind("<Return>", self.OnPressEnter)
        self.entry4.bind("<Return>", self.OnPressEnter)
        self.entry5.bind("<Return>", self.OnPressEnter)
        self.entry6.bind("<Return>", self.OnPressEnter)
        
        self.labelVariable = Tk.StringVar()
        label = Tk.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=6,columnspan=2,sticky='EW')


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
        


    def OnPressEnter(self,event):
        n1 = self.entryVariable1.get()
        n2 = self.entryVariable2.get()
        n3 = self.entryVariable3.get()
        n4 = self.entryVariable4.get()
        n5 = self.entryVariable5.get()
        n6 = self.entryVariable6.get()
        if (n1 == '') or (n2 == '') or (n3 == '') or (n4 == '') or (n5 == '') or (n6 == ''):
            self.labelVariable.set("You need to enter every value")
            return
        self.manager = Manager(int(n1), int(n2), int(n3), int(n4), int(n5), int(n6))#TODO
        text = dict()
        percent = dict()
        pollution = dict()
        Pollution = dict()
        for i in range(25):
            
            Control = Control_data(self)
            self.master.wait_window(Control.top)
            self.manager.main()
            if (i == 0):
                man = self.manager
                self.x = np.linspace(0, int(man.Town.Area[0]), 100)
                self.y = np.linspace(0, int(man.Town.Area[1]), 100).reshape(-1, 1)
                im = self.ax.imshow(f(self.x, self.y, man.Town.Companies, man.Town.Cars.made_pollution - man.Weather), cmap='YlOrRd', vmin = 25000, vmax = 500000, animated=False)
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
                    self.ax.text(x, y, company.name, style='italic')
                    text[company] =  self.ax.text(5 + x, 5 + y, "filters: %d" %(company.filters), style='italic')
                    percent[company] = self.ax.text(10 + x, 10 + y, "%" + "%d" %(round(company.day_count * (100.0/7))), style='italic')
                    pollution[company] = self.ax.text(10 + x, 15 + y, "pollution: %.2f" %(company.daily_pollution), style='italic')
                Fund = self.ax.text(30, 30, "Fund: %d" %(self.manager.Town.Fund))
                count = 0
                for point in self.manager.Town.points:
                    c1, c2 = point
                    Pollution[point] = self.ax.text(c1, c2, "Pollution: %.2f" %(self.manager.Town.Pollution[count]))
                    count += 1
                
            else:
                im.set_array(f(self.x, self.y, self.manager.Town.Companies, self.manager.Town.Cars.made_pollution - man.Weather))
                for company in self.manager.Town.Companies:
                    text[company].set_text("filters: %d" %(company.filters))
                    percent[company].set_text("%" + "%d" %(round(company.day_count * (100.0/7))))
                    pollution[company].set_text("pollution: %.2f" %(company.daily_pollution))
                Fund.set_text("Fund: %d" %(self.manager.Town.Fund))
                count = 0
                for point in self.manager.Town.points:
                    Pollution[point].set_text("Pollution: %.2f" %(self.manager.Town.Pollution[count]))
                    count += 1
                
            self.canvas.draw()
            
            
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
                
        
def f(x, y, Companies, car_pollution):
    poll = np.zeros((len(x), len(y)))
    constant = 1000#TODO
    poll += car_pollution
    for company in Companies:
        c1, c2 = company.location
        s = company.size
        c1 += s/4
        c2 += s/4
        poll += constant * company.made_pollution/((x-c1)*(x-c1) + (y-c2)*(y-c2))#TODO devision by zero
    return poll


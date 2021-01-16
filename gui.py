import tkinter as tk
from calc import calculations
class gui():
    #A example plot button for graphs
    def input(self):
        self.type=self.entry.get()
        return
    def rootApp(self):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.resizable(width=False, height=False)
        self.root.title("Data Analysis")
        self.p1 = tk.PhotoImage(file='comp.png')
        self.root.iconphoto(False, self.p1)
        return
    def frames(self):
        #Background color
        self.bFrame = tk.Frame(self.root,bd=5,bg='#024879')
        self.bFrame.place(relx=.5,rely=0,relwidth=1,relheight=1,anchor='n')
        #Front Frame
        self.Fframe = tk.Frame(self.root,bd=5,bg='#b4ff9f')
        self.Fframe.place(relx=.5,rely=.05,relwidth=.90,relheight=.9,anchor='n')
        return
    def labels(self):
        self.title = tk.Label(self.root,bg='#b4ff9f',fg='#2980b9',text='Data Analysis', font=60)
        self.title.place(relx=.5, rely=0.10, relwidth=0.13, relheight=.025, anchor='n')
        self.instru = tk.Label(self.root, bg='#2980b9', fg='#b4ff9f', text='On the left side are\n Preset data models to select\n Down Below is text field to \nspecify Conference to plot\n Ran out of time for\n This version\n\n\n\n\nCreated By:\nJohn Parkhurst', font=60)
        self.instru.place(relx=.85, rely=0.59, relwidth=0.17, relheight=.35, anchor='n')
        return
    def buttons(self):
        self.plot_button = tk.Button(master=self.Fframe,bd=3,text="Plot",bg='#2980b9',fg='#b4ff9f',font='sans 16 bold',command=lambda: [self.ourCalc.plot(self),self.input(),self.entry.insert(0,self.type)])
        self.plot_button.place(relx=.5, rely=0.70, relwidth=0.13, relheight=.05, anchor='n')
        #This is the button side bar, for type of graph
        self.three_button = tk.Button(master=self.Fframe,bd=5,text="Conference 3's",bg='#2980b9',fg='#b4ff9f',font='sans 16 bold',command=lambda: [self.ourCalc.plot3P(self)])
        self.three_button.place(relx=.1,rely=.2,relwidth=.175,relheight=.1,anchor='n')
        self.wins_button = tk.Button(master=self.Fframe, bd=5, text="Conference Wins", bg='#2980b9', fg='#b4ff9f',font='sans 16 bold', command=lambda: [self.ourCalc.plotWins(self)])
        self.wins_button.place(relx=.1, rely=.3, relwidth=.175, relheight=.1, anchor='n')
        self.bar_button = tk.Button(master=self.Fframe,bd=5, text="Shot Breakdown", bg='#2980b9', fg='#b4ff9f',font='sans 16 bold',command=lambda: [self.ourCalc.plotTot(self)])
        self.bar_button.place(relx=.1, rely=.4, relwidth=.175, relheight=.1, anchor='n')
        self.density_button = tk.Button(master=self.Fframe, bd=5, text="Offense Vs\n Defense", bg='#2980b9', fg='#b4ff9f',font='sans 16 bold', command=lambda: [self.ourCalc.plotOVD(self)])
        self.density_button.place(relx=.1, rely=.5, relwidth=.175, relheight=.1, anchor='n')
        return
    def fields(self):
        #self.field = tk.Text(self.Fframe, bg='#2980b9', fg='yellow', bd=5)
        #self.field.place(relwidth=.5, relheight=.2, relx=.25, rely=.8)
        #This is the input field
        self.entry = tk.Entry(self.Fframe, font=40, bg='#2980b9', fg='yellow')
        self.entry.place(relwidth=0.5, relheight=.2, relx=.25, rely=.8)
        return
    def __init__(self):
        #Just importing our calculations to the
        self.ourCalc = calculations()
        #Select the desired year
        self.year = 2000
        #The variable we set from the text field
        #The Tkinter Window itself
        self.rootApp()
        # Used to distinguish the different types of graphs wanted
        self.type = tk.StringVar(self.root)
        #The frames to group and place other objects on
        self.frames()
        #The Labels like the title
        self.labels()
        #The Buttons
        self.buttons()
        #This is the main fields and entry features
        self.fields()
        self.root.mainloop()


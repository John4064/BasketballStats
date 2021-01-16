from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
import tkinter as tk
class calculations():
    def dataImport(self):
        self.df = pd.read_csv("cbb18.csv")
        return
    def plotWins(self,gui):
        self.figure1 = plt.Figure(figsize=(3,3),dpi=100)
        ax1=self.figure1.add_subplot(111)
        #Grouping the figures
        grouped = self.df.groupby(self.df.CONF)
        ACC_df = grouped.get_group("ACC")
        B12_df = grouped.get_group("B12")
        BE_df = grouped.get_group("BE")
        #plotting them by conference with w/g to calculate win% and EFG_O being the Y
        #color coded to facilitate readability.
        ax1.plot((ACC_df['W'] / ACC_df['G']), ACC_df['EFG_O'], 'bo')
        ax1.plot((B12_df['W'] / B12_df['G']), B12_df['EFG_O'], 'go')
        ax1.plot((BE_df['W'] / BE_df['G']), BE_df['EFG_O'], 'ro')
        ax1.axis([0.2, 1, 46, 60])
        ax1.set_xlabel('Win Percentage')
        ax1.set_ylabel('Effective Field Goal Percentage')
        ax1.legend(['ACC', 'Big 12', 'Big East'])
        scat = FigureCanvasTkAgg(self.figure1,gui.Fframe)
        scat.get_tk_widget().place(relx=.5, rely=.10, relwidth=.40, relheight=.55, anchor='n')
        return
    def plotHist(self,gui):
        self.fig = Figure(figsize=(5, 5), dpi=100)
        ax2 = self.fig.add_subplot(111)
        self.df.hist(['G'])
        gui.canvas = FigureCanvasTkAgg(self.fig, master=gui.Fframe)
        gui.canvas.draw()
        gui.canvas.get_tk_widget().place(relx=.5, rely=.15, relwidth=.40, relheight=.5, anchor='n')
        return
    def plot(self,gui):
        self.fig = Figure(figsize=(5, 5), dpi=100)
        y = [i ** 2 for i in range(101)]
        plot1 = self.fig.add_subplot(111)
        plot1.plot(y)
        gui.canvas = FigureCanvasTkAgg(self.fig, master=gui.Fframe)
        gui.canvas.draw()
        gui.canvas.get_tk_widget().place(relx=.5, rely=.10, relwidth=.40, relheight=.55, anchor='n')
        return
    def plot3P(self,gui):
        self.figure2 = plt.Figure(figsize=(3, 3), dpi=100)
        ax2 = self.figure2.add_subplot(111)
        grouped = self.df.groupby(self.df.CONF)
        ACC_df = grouped.get_group("ACC")
        B12_df = grouped.get_group("B12")
        BE_df = grouped.get_group("BE")
        ax2.plot((ACC_df['3P_D']), ACC_df['3P_O'], 'bo')
        ax2.plot((B12_df['3P_D']), B12_df['3P_O'], 'go')
        ax2.plot((BE_df['3P_D']), BE_df['3P_O'], 'ro')
        ax2.axis([29, 40, 29, 41])
        ax2.set_xlabel('3P%')
        ax2.set_ylabel('Opponent 3p%')
        ax2.legend(['ACC', 'Big 12', 'Big East'])
        scat2 = FigureCanvasTkAgg(self.figure2, gui.Fframe)
        scat2.get_tk_widget().place(relx=.5, rely=.10, relwidth=.40, relheight=.55, anchor='n')
        return
    def plotOVD(self,gui):
        self.fig5 = plt.figure()
        ax5 = self.fig5.add_subplot(111)
        grouped = self.df.groupby(self.df.CONF)
        ACC_df = grouped.get_group("ACC")
        ACC_stat = ACC_df['2P_O'] / ACC_df['2P_D']

        B10_df = grouped.get_group("B10")
        B10_stat = B10_df['2P_O'] / B10_df['2P_D']
        BE_df = grouped.get_group("BE")
        BE_stat = BE_df['2P_O'] / BE_df['2P_D']
        P12_df = grouped.get_group("P12")
        P12_stat = P12_df['2P_O'] / P12_df['2P_D']

        ax5.bar("ACC", ACC_stat, color='b', width=0.8)
        ax5.bar("Big 10", B10_stat, color='g', width=0.8)
        ax5.bar("Big East", BE_stat, color='r', width=0.8)
        ax5.bar("Pac 12", P12_stat, color='y', width=0.8)
        ax5.set_ylim(ymin=1)
        #ax5.set_xlabel('Conferences')
        ax5.set_ylabel('2P Off VS Def Shot %')
        bar = FigureCanvasTkAgg(self.fig5, gui.Fframe)
        bar.get_tk_widget().place(relx=.5, rely=.10, relwidth=.40, relheight=.55, anchor='n')
        return
    def plotTot(self,gui):
        #This plots total Wins
        self.fig6 = plt.figure()
        ax6 = self.fig6.add_subplot(111)
        grouped = self.df.groupby(self.df.CONF)
        ACC_df = grouped.get_group("ACC")
        B10_df = grouped.get_group("B10")
        BE_df = grouped.get_group("BE")
        P12_df = grouped.get_group("P12")
        ax6.set_ylabel("Wins")
        ax6.bar("ACC", ACC_df['W'], color='b', width=0.8)
        ax6.bar("Big 10", B10_df['W'], color='g', width=0.8)
        ax6.bar("Big East", BE_df['W'], color='r', width=0.8)
        ax6.bar("Pac 12", P12_df['W'], color='y', width=0.8)
        ax6.set_ylim(ymin=20)
        bar = FigureCanvasTkAgg(self.fig6, gui.Fframe)
        bar.get_tk_widget().place(relx=.5, rely=.10, relwidth=.40, relheight=.55, anchor='n')
    def __init__(self):
        self.dataImport()

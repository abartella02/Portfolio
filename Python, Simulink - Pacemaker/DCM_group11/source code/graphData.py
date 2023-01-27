import tkinter
from ttkthemes import themed_tk as tk
from tkinter import Button, IntVar, ttk,messagebox, font
from helpers import enableFrame, disableFrame, getRate

from serialcomm import recieveSignal
import random
from itertools import count

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
from functools import partial

def close():
    try:
        root.destroy()
        plt.close()
    except:
        print("Could not close graphData")

def animate(i, mode, userinfo):
    (atr, vent) = recieveSignal(userinfo)
    #atr = random.randint(0,5) ##############TEMPORARY
    #vent = random.randint(0, 5)
    xPts.append(next(index))
    if len(xPts)> maxlength:
        xPts.pop(0)
        vPts.pop(0)
        aPts.pop(0)
    vPts.append(atr)
    aPts.append(vent)
    #plt.gcf().set_size_inches(2,2)
    if mode == 'ventricular':
        V_axis = (plt.gcf().get_axes())[0]
    elif mode == 'atrial':
        A_axis = (plt.gcf().get_axes())[0]
    elif mode == 'both':
        V_axis, A_axis = plt.gcf().get_axes()
        #root.geometry("1000x500")
    

    if mode == 'ventricular' or mode == 'both':
        V_axis.cla()
        V_axis.set(xlabel="time elapsed ({})".format(getRate(rate)), ylabel="Ventricle Signal (V)")
        V_axis.plot(xPts, vPts)
    if mode == 'atrial' or mode == 'both':
        A_axis.cla()
        A_axis.set(xlabel="time elapsed ({})".format(getRate(rate)), ylabel="Atrium Signal (V)")
        A_axis.plot(xPts, aPts)
    
    


def display(mode, userinfo, frame):
    mode = mode.lower()
    if mode == 'select':
        messagebox.showerror("Graphing", "Select a mode")
        return 

    #mode: "Ventricular", "Atrial", "Both"
    global xPts
    global vPts
    global aPts
    global index
    global rate
    global maxlength
    xPts = []
    vPts = []
    aPts = []
    index = count()

    global root
    global masterFrame
    theme = "scidblue"
    #root = tk.ThemedTk()
    root = tkinter.Toplevel()
    #root.set_theme(theme) #fitting themes: breeze, scidblue
    root.title("EGram graphs")
    root.iconbitmap(r"./images/menghi.ico")
    style = ttk.Style()
    #root.grab_set()
    disableFrame(frame)

    #create frame to size the window
    masterFrame = ttk.Frame(root)
    #masterFrame.configure(width=300, height=200)
    masterFrame.pack(fill='both', expand=True, pady=5, padx=5)
    masterFrame.pack_propagate(0)

    #root.geometry("700x500")

    root.protocol(
        "WM_DELETE_WINDOW", 
        lambda:[
            enableFrame(frame),
            close()
        ]
    )

    plt.style.use("ggplot")
    plot1 = plt.gcf()

    if mode == 'both':
        plot1.subplots(1,2)
        ttk.Label(masterFrame, 
            text = "Ventricular Signal\t\t\t\tAtrial Signal",
            font = ("Calibri", 18)
            ).pack()
        root.minsize(1100, 500)
    else:
        plot1.subplots(1,1)
        ttk.Label(masterFrame, 
            text = "{} Signal".format(mode.title()),
            font = ("Calibri", 18)
            ).pack()
        root.minsize(700, 500)

    canvas = FigureCanvas(plot1, master=masterFrame)
    canvas.get_tk_widget().pack(fill='both', expand=True, ipadx=20, ipady=20, padx=10, pady=10)

    #rate
    rate = 1
    maxlength = 30

    if rate == 1000:
        maxlength = 10
    elif rate == 100:
        maxlength = 20
    elif rate == 10:
        maxlength = 30
    elif rate == 1:
        maxlength = 40

    animatedPlot = FuncAnimation(plot1, partial(animate, mode=mode, userinfo=userinfo), interval=rate, blit=False)
    root.mainloop()

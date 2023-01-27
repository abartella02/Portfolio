from tkinter import messagebox
import json
from serialcomm import findDevice
import threading as T
import time

class ClassVar:
    def __init__(self):
        self.value = None
        pass
    def set(self, val):
        self.value = val
    def get(self):
        return self.value

def getRate(rate):
    if rate == 1:
        return 'ms'
    elif rate == 10:
        return '1/100 secs'
    elif rate == 100:
        return '1/10 secs'
    elif rate == 1000:
        return 's'
    else:
        return 'cycles'

def changeButton(button, style, frame):
    if button['text'] == "Connect":
        button.configure(text="Disconnect")
        style.configure('connectionImage.TFrame', background="green")
        frame.grid(row=3, column=0, sticky='ew')
        frame.grid_columnconfigure(0, weight=1)
    else:
        button.configure(text="Connect")
        style.configure('connectionImage.TFrame', background="red")
        frame.grid_forget()
    button.update()

def clearFrame(frame): #clear all existing widgets from tkinter frame
    try:
        for i in frame.winfo_children(): #iterating through widgets
            i.destroy()
    except:
        print('**CLEARFRAME ERROR')

def disableFrame(frame):
    try:
        for i in frame.winfo_children(): #iterating through widgets
            i.config(state="disabled")
    except:
        print('**DISABLEFRAME ERROR')

def enableFrame(frame):
    try:
        for i in frame.winfo_children(): #iterating through widgets
            i.config(state="enabled")
    except:
        print('**DISABLEFRAME ERROR')

def checkEmptyCredentials(username, password): #check if login info is blank
    if username == '' or password == '':
        return True

def checkInvalidChars(username):
    invalidStrs = ['&', '=', '_', '+', ',', '<', '>', 
        '..', '/', '\\', '\'', '"', '$', '\#', '!', 
        '(', ')', '*', ':', ';', '@', '[', ']', '^', 
        '`', '{', '|', '}', '~']

    for i in invalidStrs:
        if i in username:
            return False
    return True


def printParamVals(parameters, spin, widgets): #get new parameter values from GUI
    for i in parameters: #iterating through dictionary
        p = parameters[i]
        if p in widgets: #check that parameter is not blank
            cur = spin[p["Name"]].get() #get current value from GUI spinbox
            if float(cur) in p['Range']: #check if value is in acceptable range
                p["Value"] = float(cur)
            else:
                messagebox.showwarning("Parameter Editor", "Invalid Value for {}".format(p["Name"]))
                p["Value"] = None #reset current value to noneType
            print(p["Name"], p["Value"])

def updateParams(parameters, userinfo):
    #print(json.dumps(parameters, indent=1))
    if parameters["UpperRateLimit"]["Value"] < parameters["LowerRateLimit"]["Value"]:
        messagebox.showwarning("Invalid Parameters", "Error: LRL cannot be greater then URL")
        return
    with open(userinfo["filepath"], "w") as f: 
        f.write(json.dumps(parameters, indent=2))

def resizeWindow(root, width, height):
    w_width = root.winfo_width()
    w_height = root.winfo_height()

    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()

    x = s_width//2 - w_width//2
    y = s_height//2 - w_height//2

    root.geometry("{}x{}".format(width, height))
    root.minsize(width, height)

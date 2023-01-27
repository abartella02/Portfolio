import serial
import serial.tools.list_ports
import json
import time
import struct
from tkinter import messagebox


def findDevice():
    with open(r"./data/pacemakerData.json", "r") as f:
        data = json.load(f)

    ports = serial.tools.list_ports.comports()
    if len(ports) == 0: 
        #messagebox("connect the thing")
        print("\n**********Device Not Connected************\n")
        return None

    for p in ports:
        #print(p.serial_number)
        if str(p.serial_number) == str(data["Serial Number"]):
            return p
    return None

def getParamData(userinfo):
    with open(userinfo["filepath"]) as f:
        parameters = json.load(f)
    return parameters

def sendData(ser, signalSet):
    ser.write(b'\x16' + b'\x55' + signalSet)

def recieveParams(ser, signalSet):
    print("enter")
    ser.write(b'\x16' + b'\x22' + signalSet) #start, sync, signal

    rec = {}
    print("read start")
    data = ser.read(64)
    print("read end")
    rec["MODE"] = struct.unpack("H", data[0:2])[0]
    rec["LowerRateLimit"] = struct.unpack("H", data[2:4])[0]
    rec["UpperRateLimit"] = struct.unpack("H", data[4:6])[0]

    rec["APulseAmplitude"] = struct.unpack("d", data[6:14])[0]
    rec["VPulseAmplitude"] = struct.unpack("d", data[14:22])[0]
    rec["APulseWidth"] = struct.unpack("d", data[22:30])[0]
    rec["VPulseWidth"] = struct.unpack("d", data[30:38])[0]
    rec["ASensitivity"] = struct.unpack("d", data[38:46])[0]
    rec["VSensitivity"] = struct.unpack("d", data[46:54])[0]

    rec["VRP"] = struct.unpack("H", data[54:56])[0]
    rec["ARP"] = struct.unpack("H", data[56:58])[0]
    rec["PVARP"] = struct.unpack("H", data[58:60])[0]
    rec["Hysterisis"] = struct.unpack("H", data[60:62])[0]
    rec["RateSmoothing"] = struct.unpack("H", data[62:64])[0]
    
    print("Recieved Data\n", json.dumps(rec, indent=1))

    if len(rec) != 0:
        messagebox.showinfo("Connect", "Parameters Recieved!")
    else:
        messagebox.showinfo("Connect", "An error occured when reading from pacemaker")
    return rec

def makeSignalSet(mode, parameters):
    paramDict = {}

    modeNum = 0
    if mode == "AOO":
        modeNum = 1
    elif mode == "VOO":
        modeNum = 2
    elif mode == "AAI":
        modeNum = 3
    elif mode == "VVI":
        modeNum = 4

    paramDict["Mode"] = int(modeNum)

    signalSet = struct.pack("H", modeNum)

    #print("Mode:", modeNum, "({})".format(mode))

    for key in parameters.keys():
        p = parameters[key]
        n = p["Name"]
        val = p["Value"]
        #print(n, val)
        if  n == "Atrial Pulse Amplitude" or n == "Ventricular Pulse Amplitude" or n == "Atrial Pulse Width" or n == "Ventricular Pulse Width" or n == "Atrial Sensitivity" or n == "Ventricular Sensitivity":
            if val == None:
                val = 0
            paramDict[n] = float(val)
            signalSet += struct.pack("d", float(val))
        else:
            if val == None:
                val = 0
            paramDict[n] = int(val)
            signalSet += struct.pack("H", int(val))
    #print("Length of Signal Set:",len(signalSet))
    return signalSet




#########################################################################

def recieveSignal(userinfo):
    signalSet = makeSignalSet("VOO", getParamData(userinfo))
    try:
        with serial.Serial(findDevice().device, 115200, timeout = 5) as ser:
            #print("enter")
            ser.write(b'\x16' + b'\x33' + signalSet) #start, sync, signal

            data = ser.read(64)

            atr = None
            vent = None

            atr = float(struct.unpack("d", data[0:8])[0])
            vent = float(struct.unpack("d", data[8:16])[0])
        return (atr, vent)
    except:
        print("Signal get timeout")
    return None, None

def sendParams(userinfo, mode):
    signalSet = makeSignalSet(mode, getParamData(userinfo))
    try:
        with serial.Serial(findDevice().device, 115200, timeout=5) as ser:
            sendData(ser, signalSet)
        
        print("Data Sent")
        messagebox.showinfo("Send", "Parameters Sent!")
    except:
        print("Data send timeout")
        messagebox.showwarning("Recieve", "An error occurred while sending data to pacemaker")

def getParams(userinfo, mode):
    signalSet = makeSignalSet(mode, getParamData(userinfo))
    try:
        #print("FIND DEVICE DATA: ", findDevice().description,",", findDevice().serial_number)
        with serial.Serial(findDevice().device, 115200, timeout = 5) as ser:
            r = recieveParams(ser, signalSet)
    except:
        print("Parameter get timeout")
        messagebox.showwarning("Recieve", "An error occurred while getting data from pacemaker")
        return None
    
    try:
        with open(userinfo['filepath'], 'r') as f:
            params = json.load(f)
            for name in params.keys():
                params[name]['Value'] = r[name]
            print('parameters loaded')
    except:
        print('parameters not loaded')


    messagebox.showinfo("Recieve", "Parameters Recieved")
    
    return r



def main(userinfo, mode):
    '''
    device = findDevice()
    if device == None:
        print("Device not found")
        return
    print(device.description)
    '''

    parameters = getParamData(userinfo)

    signalSet = makeSignalSet(mode, parameters)

    '''
    with serial.Serial(device.device, 115200) as ser:
        print("Port open?", ser.is_open) #port is open
        print("SignalSet:", signalSet)
        sendData(ser, signalSet)
        #print("***Data sent")
        recieveData(ser, signalSet)
        print("***Data recieved")
    '''
    print(signalSet)

'''with open(r"./data/userpass.json", "r") as f:
    data = json.load(f)
data = data[0]'''

#main(data, "VOO")

#This script was written to minimize the time needed to fill a macro-enabled dynamic excel document with subcontractor information
#included in this folder are sample files which can be used to demonstrate its functionality
#note that the sample files mentioned use generic company names

#there is intention to use tkinter to add a GUI, implementation is in progress

#sublist sorter V1.2 - switched to xlwings to preserve macros

#!!!!!!!
#*************************************************************************
#PLEASE CLOSE EXCEL BEFORE USING, OR ELSE THE SCRIPT WILL CLOSE IT FOR YOU
#*************************************************************************
#!!!!!!!


import textract
from xlwings import *
import time
import os
import pathlib

try: #close excel before starting
    os.system("TASKKILL /F /IM EXCEL.EXE")
except:
    pass

global path
path = pathlib.Path(__file__).parent.absolute()
print('Starting...')

global subinfo
subinfobook = Book('Sub Info.xlsx')
subinfo = subinfobook.sheets[0]
print("Sub Info opened")

global dynamic
dynamicbook = Book('template.xlsm')
dynamic= dynamicbook.sheets[0]
print('Template Opened')

global sublist
sublist = textract.process('Sub List.docx').decode('utf-8')

print("Subcontractor Info Retrieved \n")


def columnlist(column_letter, sheet):
    mylist = []
    for cell in sheet[str(column_letter)]:
        if cell.value == '':
            break
        else:
            mylist.append(cell.value)
    res = [' ' if v is None else v for v in mylist]
    return res



def sort_subtrades(sublist):
    temp = sublist.split('\n')

    sublist = sublist.replace('\n\n', '\n')
    
    source_subdict = {}
    source_sublist = []
    for i in temp:
        if i == '':
            temp.remove('')
    
    source_subdict['Job'] = temp[0]
    global job_name
    job_name = temp[0]
    
    titles = []
    subs = []
    for i in range(0, len(temp)):
        if i%2 == 1:
            titles.append(temp[i])
        if i%2 == 0 and i != 0:
            subs.append(temp[i])

    for i in range(0, len(subs)):
        source_subdict[str(titles[i])] = subs[i]
        source_sublist.append([titles[i], subs[i]])
    
    return source_sublist, source_subdict

def sub_list(subtrade):
    subs = subtrade[1].split(';')

    #remove formatting for 'Name <email>'
    for i in subs:
        if '>' in i:
            index = subs.index(i)
            temp = i.rstrip('>')
            temp = temp.split('<')
            #i = temp[1]
            subs[index] = temp[1] #i

    temp1 = {}
    temp0 = []
    #remove formatting for " Name 'email' "
    for i in subs:
        i = i.replace("'", "").strip().lower()
        temp0.append(i)
    temp1['Emails'] = temp0

    temp1['Subtrade'] = subtrade[0]

    return temp1


def get_info():
    print('getting info...')
    masterlist = []
    '''
    info = {
    'Name' : ''
    'Email' : ''
    'Nums' : ''
    }
    '''
    i = 1
    while(subinfo['L{}'.format(i)].value != None):
        info = {}
        info['Name'] = subinfo['A{}'.format(i)].value
        info['Nums'] = subinfo['L{}'.format(i)].value
        info['Email'] = subinfo['P{}'.format(i)].value

        masterlist.append(info)

        i+= 1

        if i>1000:
            break
    print('information acquired, continuing')
    return masterlist

def find_numbers(one_sub, masterlist):
    info  = {}
    print(one_sub)
    #input("input: ")
    '''
    info = {
    'Name' : ''
    'Email' : ''
    'Nums' : ''
    }
    '''
    info['Email'] = one_sub
    info['Name'] = ''
    info['Nums'] = ''
    #print(subinfo['L5'].value)
    for i in masterlist:
        if info['Email'].lower() in i['Email'].lower():
            info['Name'] = i['Name']
            info['Nums'] = i['Nums']


    '''
    i = 1
    while (i<900):
        value = str(subinfo['P{}'.format(i)].value)

        if info['Email'] in value.lower():
            try:
                print(value + " | " + str(i))
            except:
                continue
            info['Nums'] = subinfo['L{}'.format(i)].value
            info['Name'] = subinfo['A{}'.format(i)].value
        i+= 1
    '''
    return info




def write_to(source_sublist):
    #source_sublist = sort_subtrades(sublist)[0]
    x = sub_list(source_sublist[0])['Emails']
    print("benchmark")
    all_info = []
    masterlist = get_info()
    for i in x:
        all_info.append( find_numbers(i, masterlist) )
        time.sleep(2)
        print(all_info[-1])

    '''
    #group together emails with missing info but same address
    for i in all_info:
        if len(i) < 3:
            for j in all_info:
                if j['Email'].endswith(  i['Email'].split('@')[1]  ) and len(j) == 3:
                    j['Email'] = str(j['Email'] + ';' + i['Email'])
    '''

    #subtrades index
    #subtrades_index = open("subtrades index.txt", "r")
    
    if 'demo' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [4, 50]
    elif 'shoring' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [53, 100]
    elif 'fencing' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [103, 150]
    elif 'mechanical' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [154, 200]
    elif 'rebar' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [203, 252]
    elif 'steel' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [255, 304]
    elif 'barriers' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [307, 356]
    elif 'electrical' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [359, 408]
    elif 'formwork' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [411, 460]
    elif 'automatic doors' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [463, 512]
    elif 'caulking' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [515, 564]
    elif 'communication' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [567, 616]
    elif 'doors/frames' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [619, 668]
    elif 'drywall' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [671, 720]
    elif 'elevators' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [723, 772]
    elif 'fall arrest' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [775, 824]
    elif 'fire alarm' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [827, 876]
    elif 'flooring' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [879, 928]
    elif 'landscaping' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [931, 980]
    elif 'louvers' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [983, 1032]
    elif 'masonry' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1035, 1084]
    elif 'siding' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1087, 1136]
    elif 'monitoring' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1139, 1188]
    elif 'painting' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1191, 1240]
    elif 'railing' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1243, 1292]
    elif 'roofing' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1295, 1344]
    elif 'signs' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1347, 1396]
    elif 'tree' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1399, 1448]
    elif 'watermain' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1451, 1500]
    elif 'windows' in sub_list(source_sublist[0])['Subtrade'].lower():
        subtrade = [1503, 1552]

    i = 0
    for j in range(subtrade[0], len(all_info) + subtrade[0]): #subtrade[1]):
        temp = all_info[i]
        if temp['Name'] != None and temp['Name'] != '':
            dynamic.range(j, 2).value = temp['Email']
            #try:
                #dynamic['c{}'.format(str(j))].value = all_info[i]['Nums']
            dynamic.range(j, 3).value = temp['Nums']
            #except:
                #dynamic['c{}'.format(str(j))].value = ''
                #dynamic.range(3, j).value = ''
            #try:
                #dynamic['a{}'.format(str(j))].value = all_info[i]['Name']
            dynamic.range(j, 1).value = temp['Name']
            #except:
                #dynamic['c{}'.format(str(j))].value = all_info[i]['Email'].split('@')[1].split('.')[0]
                #dynamic.range(1, j).value = all_info[i]['Email'].split('@')[1].split('.')[0]
        i+=1

    dynamic.range(1,1).value = job_name.title()
    
    #global filename
    #filename = str(input('Input file name:  ') + '.xlsm')
    filename = "New Filled Template.xlsm"
    try:
        os.remove(r'{}\{}'.format(path, filename)) #overwrites file of the same name
    except:
        pass

    return filename


#print(sort_subtrades(sublist)[0])
filename = write_to(sort_subtrades(sublist)[0])
print("write_to finished")
dynamicbook.save(r'{}\{}'.format(path, filename))
dynamicbook.close()
subinfobook.close()

print('opening...')

os.startfile(r'{}\{}'.format(path, filename))

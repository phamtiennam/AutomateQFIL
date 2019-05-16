#Using python 3.6.8
#Link: https://www.python.org/downloads/release/python-368/
import pyautogui
import time
import os
import sys
import subprocess
startQFIL = "startQFIL.ps1"

#class StartQFIL:
def InitializeQFIL():
    print("StartQFIL...............")
    try:
        cmd="powershell" + "  " + ".\\" + startQFIL
        subprocess.call(cmd)
    except OSError:  
        print("NOT ABLE TO EXECUTE QFIL")
        sys.exit(1)

    SelectPort = pyautogui.locateOnScreen("SelectPort.png")

    while SelectPort is None :
        print("Loading QFIL.")
        SelectPort = pyautogui.locateOnScreen("SelectPort.png")
        time.sleep(2)

    print("Initialize QFIL Done ...")
    
def locationOnScreen(pic_name,icrs_x,decre_x,icrs_y,decre_y):
    print("icrs_y:",icrs_y)
    x, y = pyautogui.locateCenterOnScreen(pic_name)
    print("x:",x)
    print("y:",y)
    x += icrs_x
    x -= decre_x
    y = y + icrs_y
    #y = y + 50
    print("y1:",y)
    y -= decre_y
    print("x1:",x)
    
    return x,y

def locateThenLeftClick(pic_name,icrs_x,decre_x,icrs_y,decre_y):
    print("icrs_y_0:",icrs_y)
    x,y = locationOnScreen(pic_name,icrs_x,decre_x,icrs_x,decre_y)
    pyautogui.click(x, y)
    time.sleep(1)
    
def locateThenDoubleClick(pic_name,icrs_x,decre_x,icrs_y,decre_y):
    x,y = locationOnScreen(pic_name,icrs_x,decre_x,icrs_x,decre_y)
    pyautogui.doubleClick(x,y)
    time.sleep(1)

def file_get_contents(filename):
    with open(filename, 'r') as f:
        return f.read()

def provisioning():
    '''
    locateThenLeftClick("SelectPort.png", 0, 0, 0, 0)
    locateThenLeftClick("OK_button.png", 0, 0, 0, 0)
    locateThenLeftClick("Configuration.png", 0, 0, 0, 0)
    locateThenLeftClick("FileHoseConfiguration.png", 0, 0, 0, 0)
    locateThenLeftClick("Provision.png", 0, 0, 0, 0)
    locateThenLeftClick("OK_button.png", 0, 0, 0, 0)

    ProgrammerPath = file_get_contents(os.path.join('.','Path', 'ProgrammerPath.txt'))
    locateThenLeftClick("ProgrammerPath.png", 50, 0, 0, 0)
    print(ProgrammerPath)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(ProgrammerPath)

    ProvisionXml = file_get_contents(os.path.join('.','Path', 'ProvisionXml.txt'))
    locateThenLeftClick("ProvisionXml.png", 70, 0, 0, 0)
    print("000000000000000000000000000000")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(ProvisionXml)
    '''
    locateThenLeftClick("SelectPort_Browse.png",0,0,50,0)




#InitializeQFIL()
provisioning()








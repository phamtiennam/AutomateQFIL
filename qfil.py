#Using python 3.6.8
#Link: https://www.python.org/downloads/release/python-368/
import pyautogui
import time
import os
import sys
import subprocess
startQFIL = "startQFIL.ps1"

def checkPortAvailable():
    portAvailable = None
    portAvailable = pyautogui.locateOnScreen("images\\NoPortAvailable.png", confidence=0.8)
    if portAvailable is not None :
        print("No Port Available")
        sys.exit(1)

def gotoEDLmode():
    print("checking EDL mode...")
    adb_out = str(subprocess.check_output(["adb","devices"]))
    if("\\tdevice\\r" in adb_out):
        print("Go to EDL mode.")
        subprocess.call("adb reboot edl")
    else:
        print("adb devices not found")
        

def InitializeQFIL():
    print("Checking QFIL...............")
    try:
        cmd="powershell" + " -noprofile -executionpolicy bypass -file " + ".\\" + startQFIL
        subprocess.call(cmd)
    except OSError:  
        print("NOT ABLE TO EXECUTE QFIL")
        sys.exit(1)

    SelectPort = None

    while SelectPort is None :
        print("Loading QFIL.")
        SelectPort = pyautogui.locateOnScreen("images\\SelectPort.png", confidence=0.8)
        time.sleep(2)
    print("Initialize QFIL Done ...")
    

def file_get_contents(filename):
    with open(filename, 'r') as f:
        return f.read()


def typewrite_contents(filename):
    filecontents = file_get_contents(filename)
    pyautogui.typewrite(filecontents)
    time.sleep(2)
    
class locateMouse:
    pic_name,icrs_x,decre_x,icrs_y,decre_y = ["",0,0,0,0]
 
    def assignVal(self,inputList = []):
        self.pic_name = inputList[0]
        self.icrs_x = inputList[1]
        self.decre_x = inputList[2]
        self.icrs_y = inputList[3]
        self.decre_y = inputList[4]
        print(self.pic_name)
   
    def locationOnScreen(self):
        x, y = pyautogui.locateCenterOnScreen(self.pic_name,confidence=0.8)
        x += self.icrs_x
        x -= self.decre_x
        y += self.icrs_y
        y -= self.decre_y
        return x,y
        
    def leftClick(self,inputList = []):
        self.assignVal(inputList)
        time.sleep(3)
        x,y = self.locationOnScreen()
        pyautogui.click(x, y)
        
      
def provisioning():

    able2Provi= None
    notAble2Provi = None
    
    print("Start Provisioning...")
    a = locateMouse()
    a.leftClick(["images\\SelectPort.png", 0, 0, 0, 0])
    a.leftClick(["images\\OK_button.png", 0, 0, 0, 0])
    a.leftClick(["images\\Configuration.png", 0, 0, 0, 0])
    a.leftClick(["images\\FileHoseConfiguration.png", 0, 0, 0, 0])
    a.leftClick(["images\\DeviceType.png", 0, 0, 0, 5])
    pyautogui.move(0, 30)
    pyautogui.click()
    a.leftClick(["images\\Provision.png", 0, 0, 0, 0])
    a.leftClick(["images\\OK_button.png", 0, 0, 0, 0])
    a.leftClick(["images\\ProgrammerPath.png", 850, 0, 0, 0])
    a.leftClick(["images\\FileName.png", 100, 0, 0, 0])
    #time.sleep(16)
    typewrite_contents("Path\\ProgrammerPath.txt")
    #time.sleep(3)
    #a.leftClick(["images\\Open.png", 0, 0, 0, 0])
    a.leftClick(["images\\ProvisionXml.png", 850, 0, 0, 0])
    a.leftClick(["images\\FileName.png", 100, 0, 0, 0])
    typewrite_contents("Path\\ProvisionXml.txt")
    
    a.leftClick(["images\\Open.png", 0, 0, 0, 0])
    gotoEDLmode()
    a.leftClick(["images\\SelectPort.png", 0, 0, 0, 0])
    a.leftClick(["images\\OK_button.png", 0, 0, 0, 0])
    print("Check if provisioning is possible...")
    try:
        able2Provi= pyautogui.locateOnScreen("images\\Able2Provisioning.png")
    except OSError:
        print("Able2Provisioning.png Not Found on Screen")
       
    try:
        notAble2Provi = pyautogui.locateOnScreen("images\\NotAble2Provisioning.png")
    except OSError:
        print("NotAble2Provisioning.png Not Found On Screen")
    
    if (notAble2Provi is not None and able2Provi is None ):
        print("Not able to provisioning")
        sys.exit()
    else:
        print("able to provisioning")
        a.leftClick(["images\\Able2Provisioning.png", 0, 0, 0, 0])

def flatbuild():
    able2dl = None
    notAble2dl = None
    
    print("Flashing image(Flat Build)...")
    a = locateMouse()
    a.leftClick(["images\\SelectPort.png", 0, 0, 0, 0])
    a.leftClick(["images\\OK_button.png", 0, 0, 0, 0])
    a.leftClick(["images\\flatbuild\\FlatBuild.png", 0, 0, 0, 0])
    a.leftClick(["images\\ProgrammerPath.png", 850, 0, 0, 0])
    a.leftClick(["images\\FileName.png", 100, 0, 0, 0])
    typewrite_contents("Path\\ProgrammerPath.txt")
    
    #a.leftClick(["images\\Open.png", 0, 0, 0, 0])
    a.leftClick(["images\\flatbuild\\LoadXML.png", 0, 0, 0, 0])
    
    #for-loop for 2 times
    for i in range(1,3):
        a.leftClick(["images\\FileName.png", 100, 0, 0, 100])
        time.sleep(3)
        print("sending Ctrl A")
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(3)
        a.leftClick(["images\\Open.png", 0, 0, 0, 0])
    
    #Check if DOWNLOAD image is possible
    try:
        able2dl= pyautogui.locateOnScreen("images\\flatbuild\\Able2Download.png")
    except OSError:
        print("Able2Download.png Not Found on Screen")
       
    try:
        notAble2dl = pyautogui.locateOnScreen("images\\flatbuild\\NotAble2Dowload.png")
    except OSError:
        print("NotAble2Dowload.png Not Found On Screen")
    
    if (notAble2dl is not None and able2dl is None ):
        print("Not able to DOWNLOAD image")
        sys.exit()
    else:
        print("able to download/flash image")
        a.leftClick(["images\\flatbuild\\Able2Download.png", 0, 0, 0, 0])
 
   
InitializeQFIL()
checkPortAvailable()
provisioning()
pyautogui.confirm(text='Please manualy reset Power Supply then press OK',title='AUTO QFIL',buttons=['ok','cancle'])
InitializeQFIL()
checkPortAvailable()
flatbuild()










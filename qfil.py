#Using python 3.6.8
#Link: https://www.python.org/downloads/release/python-368/
import pyautogui
import time
import os
import sys
import subprocess
startQFIL = "startQFIL.ps1"

def pathof(subdir,filename):
    pathname=os.path.dirname(sys.argv[0]) #current dir of the script
    pathname=os.path.join(pathname,subdir,filename)
    return pathname
    

def checkPortAvailable():
    portAvailable = None
    portAvailable = pyautogui.locateOnScreen(pathof("images","NoPortAvailable.png"), confidence=0.8)
    if portAvailable is not None :
        print("No Port Available")
        sys.exit(1)

def gotoEDLmode():
    print("checking EDL mode...")
    adb_out = str(subprocess.check_output(["adb","devices"]))
    if("\\tdevice\\r" in adb_out):
        print("Go to EDL mode.")
        subprocess.call("adb reboot edl")
        time.sleep(15)
    else:
        print("adb devices not found")
        

def InitializeQFIL():
    print("Checking QFIL...............")
    try:
        cmd="powershell" + " -noprofile -executionpolicy bypass -file " + pathof(".",startQFIL)
        subprocess.call(cmd)
    except OSError:  
        print("NOT ABLE TO EXECUTE QFIL")
        sys.exit(1)

    SelectPort = None
    
    while SelectPort is None :
        print("Loading QFIL.")
        SelectPort = pyautogui.locateOnScreen(pathof("images","SelectPort.png"), confidence=0.8)
        time.sleep(2)
    print("Initialize QFIL Done ...")
    

def file_get_contents(filename):
    with open(filename, 'r') as f:
        return f.read()


def typewrite_contents(filename,addstr):
    filecontents = file_get_contents(filename) + "\\" + addstr
    print(filecontents)
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
        
    def delay4image(self,imagefile,timeout):
        found_img = None
        while found_img is None and timeout != 0 :
            timeout = timeout - 1
            found_img = pyautogui.locateOnScreen(imagefile, confidence=0.8)
            time.sleep(1)
        
    def leftClick(self,inputList = []):
        self.assignVal(inputList)
        delaytime = 6
        self.delay4image(self.pic_name,delaytime)
        x,y = self.locationOnScreen()
        pyautogui.click(x, y)
        
      
def provisioning():

    able2Provi= None
    notAble2Provi = None
    
    print("Start Provisioning...")
    a = locateMouse()
    a.leftClick([pathof("images","SelectPort.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","OK_button.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","Configuration.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","FileHoseConfiguration.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","DeviceType.png"), 0, 0, 0, 5])
    pyautogui.move(0, 30)
    pyautogui.click()
    a.leftClick([pathof("images","Provision.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","OK_button.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","ProgrammerPath.png"), 850, 0, 0, 0])
    a.leftClick([pathof("images","FileName.png"), 100, 0, 0, 0])
    
    typewrite_contents(pathof("Path","ImagePath.txt"),"prog_ufs_firehose_8996_ddr.elf")
    
    a.leftClick([pathof("images","Open.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","ProvisionXml.png"), 850, 0, 0, 0])
    a.leftClick([pathof("images","FileName.png"), 100, 0, 0, 0])
    typewrite_contents(pathof("Path","ImagePath.txt"),"provision_toshiba.xml")
    a.leftClick([pathof("images","Open.png"), 0, 0, 0, 0])
    
    gotoEDLmode()
    a.leftClick([pathof("images","SelectPort.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","OK_button.png"), 0, 0, 0, 0])
    print("Check if provisioning is possible...")
    try:
        able2Provi= pyautogui.locateOnScreen(pathof("images","Able2Provisioning.png"))
    except OSError:
        print("Able2Provisioning.png Not Found on Screen")
       
    try:
        notAble2Provi = pyautogui.locateOnScreen(pathof("images","NotAble2Provisioning.png"))
    except OSError:
        print("NotAble2Provisioning.png Not Found On Screen")
    
    if (notAble2Provi is not None and able2Provi is None ):
        print("Not able to provisioning")
        sys.exit()
    else:
        print("able to provisioning")
        a.leftClick([pathof("images","Able2Provisioning.png"), 0, 0, 0, 0])

def flatbuild():
    able2dl = None
    notAble2dl = None
    
    print("Flashing image(Flat Build)...")
    a = locateMouse()
    a.leftClick([pathof("images","SelectPort.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","OK_button.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","flatbuild\\FlatBuild.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","ProgrammerPath.png"), 850, 0, 0, 0])
    a.leftClick([pathof("images","FileName.png"), 100, 0, 0, 0])
    typewrite_contents(pathof("Path","ImagePath.txt"),"prog_ufs_firehose_8996_ddr.elf")
    
    a.leftClick([pathof("images","Open.png"), 0, 0, 0, 0])
    a.leftClick([pathof("images","flatbuild\\LoadXML.png"), 0, 0, 0, 0])
    
    #for-loop for 2 times
    for i in range(1,3):
        a.leftClick([pathof("images","FileName.png"), 100, 0, 0, 100])
        time.sleep(3)
        print("sending Ctrl A")
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(3)
        a.leftClick([pathof("images","Open.png"), 0, 0, 0, 0])
    
    #Check if DOWNLOAD image is possible
    try:
        able2dl= pyautogui.locateOnScreen(pathof("images","flatbuild\\Able2Download.png"))
    except OSError:
        print("Able2Download.png Not Found on Screen")
       
    try:
        notAble2dl = pyautogui.locateOnScreen(pathof("images","flatbuild\\NotAble2Dowload.png"))
    except OSError:
        print("NotAble2Dowload.png Not Found On Screen")
    
    if (notAble2dl is not None and able2dl is None ):
        print("Not able to DOWNLOAD image")
        sys.exit()
    else:
        print("able to download/flash image")
        a.leftClick([pathof("images","flatbuild\\Able2Download.png"), 0, 0, 0, 0])

def checkProcessStatus(process_name,fileimg,timeout):
    counter = timeout
    process_status = None
    while process_status is None and counter != 0 :
        counter = counter - 1
        process_status = pyautogui.locateOnScreen(fileimg, confidence=0.8)
        time.sleep(1)
   
    if process_status is None:
        print("Time Out:" + str(timeout) + "s." + process_name + " is failed.:( ")
        return 0
    else:
        print(process_name + " Done")
        return 1
        
def main():
    InitializeQFIL()
    checkPortAvailable()
    provisioning()
    #check if provisioning is succeed
    if (checkProcessStatus("Provisioning",pathof("images","ProvisionSucceedMessage.png"),15) != 1):
        sys.exit(1)

    confirm=pyautogui.confirm(text='Please manualy reset Power Supply then press OK',title='AUTO QFIL',buttons=['ok','cancel'])
    if confirm is "cancel":
        sys.exit(1)

    InitializeQFIL()
    checkPortAvailable()
    flatbuild()
    
if __name__ == "__main__":
    main()

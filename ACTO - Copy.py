import pyautogui
import time
import os
import datetime
import requests
import webbrowser
import zipfile
import shutil

############################## Note the directory path you are giving can be diffrent as from the project ##################################

# PSoCPRG = pyautogui.locateOnScreen('PSoCPRG.png')
# DevDFG = pyautogui.locateOnScreen('DevDFG.png')
# Functional_Tests = pyautogui.locateOnScreen('Functional_Tests.png')
# StopOnError = pyautogui.locateOnScreen('StopOnError.png')
# TestCnt = pyautogui.locateOnScreen('TestCnt.png')
# ViewLog = pyautogui.locateOnScreen('ViewLog.png')
# UsbPRG = pyautogui.locateOnScreen('UsbPRG.png')
# CLR = pyautogui.locateOnScreen('CLR.png')

script_dir = os.path.dirname(os.path.abspath(__file__))
screen_width, screen_height = pyautogui.size()                    #used to check the resolutio of the screen
WIDTH=(screen_width-1368)/2                                       #1368 is the Width of the screen resolution
HEIGHT=((screen_height-1028)/2)-(screen_height/36)                #1028 is the height if the screen resolution and screen_height/36 is the task bar ratio taken within the screen
RUNS=["DDF",'USBPD',"TypeC","LegChg","EPR"]
ARRAY=["CCG_DDF_Test_00_P5V2-1.cyacd","CCG_USBPD_Test_00_P5V2.cyacd","CCG_TypeC_Test_00_P5V2.cyacd","CCG_LegChg_Test_00_P5V2.cyacd","NPSoc5Tester.cyacd"]
DDF=["Post_ES100_PMG1S3-USB-C_Port0_US_EPR.txt","ES100_PMG1S3_Non_TBT_Port1_EPR_DFP"]
user = os.getlogin()


def programDUT():
    UsbPRG = pyautogui.locateOnScreen('UsbPRG.png')
    pyautogui.click(UsbPRG)
    time.sleep(2)
    pyautogui.write(ARRAY[4])
    pyautogui.press('enter')
    time.sleep(15)                                              # waiting time to load the Cyacd file
    PSoCPRG = pyautogui.locateOnScreen('PSoCPRG.png')
    pyautogui.click(PSoCPRG)
    time.sleep(2)
    with pyautogui.hold('alt'):
        for i in range(4):
            pyautogui.press("up")
    time.sleep(1)
    pyautogui.write("binaries\PMG1S3DUAL\GCC_ARM")
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.moveTo(screen_width/2,screen_height/2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(60)

def Acto_function(): 
    os.startfile(f"C:/Users\{user}/Desktop/PythonBasic/ValidationGUI_NightlyBuild_036/ValidationGUI_NightlyBuild/Release/Validation.exe")                # opening the validation tool
    time.sleep(5)
    TestCnt = pyautogui.locateOnScreen('TestCnt.png')
    pyautogui.click(TestCnt)
    StopOnError = pyautogui.locateOnScreen('StopOnError.png')
    pyautogui.click(StopOnError)
    programDUT()
    for x in range(1):
        UsbPRG = pyautogui.locateOnScreen('UsbPRG.png')
        pyautogui.click(UsbPRG)                       # waiting time to load the Cyacd file
        time.sleep(2)
        pyautogui.write(ARRAY[x])
        pyautogui.press('enter')
        time.sleep(30) 
        DevDFG = pyautogui.locateOnScreen('DevDFG.png')
        pyautogui.click(DevDFG)                       # Loading the DDF file 
        time.sleep(2)
        pyautogui.write(DDF[0])                       # enter the port Type 0:UFP,1:DFP
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(4)
        Functional_Tests = pyautogui.locateOnScreen('Functional_Tests.png')
        pyautogui.click(Functional_Tests)
        # test="Group Test Functional_Tests: DONE Iteration"
        a=0
        # Check(test,i)
        while(a==0):
            time.sleep(35)
            ViewLog = pyautogui.locateOnScreen('ViewLog.png')           #waiting for it to check the logs in next 30 sec
            pyautogui.click(ViewLog)
            time.sleep(3)
            with pyautogui.hold('ctrl'):                           #saving the logs 
                with pyautogui.hold('shift'):
                    pyautogui.press('s')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('alt','f4')
            time.sleep(1)
            with open(f'C:/Users\{user}/Desktop/PythonBasic/ValidationGUI_NightlyBuild_036/ValidationGUI_NightlyBuild/Release/Validation_save.txt', 'r') as file:
                # read all content from a file using read()
                content = file.read()
                # check if string present or not
                if 'Group Test Functional_Tests: DONE Iteration' in content:             # checking if the test case is over 
                    a=1
                    pyautogui.moveTo((screen_width/2),HEIGHT+10)
                    pyautogui.click()                             # just to activate the GUI
        print("moved out of the while loop")    
        ViewLog = pyautogui.locateOnScreen('ViewLog.png')
        pyautogui.click(ViewLog)
        time.sleep(3)
        with pyautogui.hold('ctrl'):
                with pyautogui.hold('shift'):
                    pyautogui.press('s')
        time.sleep(2)
        Validation_Date=datetime.datetime.now().strftime('%Y-%m-%d')
        pyautogui.write(RUNS[x])
        pyautogui.write("_")
        pyautogui.write(Validation_Date)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        CLR = pyautogui.locateOnScreen('CLR.png')
        pyautogui.click(CLR)
        time.sleep(2)

def ExtractZIP():
    # get the absolute path to the zip file
    zip_file_path = os.path.abspath(f"C:/Users\{user}/Downloads/mtb-example-pmg1s3-usbc-dock.zip")
    # set the path to where you want to extract the zip file
    extract_path = f"C:/Users\{user}/Desktop/PythonBasic/HexFile"
    shutil.rmtree(f"C:/Users\{user}/Desktop/PythonBasic/HexFile")
    time.sleep(2)
    os.mkdir(f"C:/Users\{user}/Desktop/PythonBasic/HexFile")
    # extract the contents of the zip file
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    time.sleep(3)
    os.remove(zip_file_path)
    
version_number = 139   
while(1):                                                               #In a loop which will continously run 
    while(1):
        # Set the base URL and version number
        base_url = "https://artifactory.icp.infineon.com/artifactory/gen-pss-wcs-sw-local/dock/mtb-example-pmg1s3-usbc-dock/release/mtb-example-pmg1s3-usbc-dock-1.0.0"
        

        # Construct the URL for the ZIP file with the new version number
        url = f"{base_url}/{version_number}/mtb-example-pmg1s3-usbc-dock.zip"

        response = requests.get(url)
        data = response.content
        with open("data.txt", "wb") as f:
            # Write the contents of the data variable to the file
            f.write(data)
        with open("data.txt", "rb") as f:
            # Read the first two bytes of the file
            magic_number = f.read(2)
            
            # Convert the bytes to a string
            magic_number_str = magic_number.decode()
            
            # Check if the magic number is "PK"
            if magic_number_str == "PK":
                print("File Found",version_number)
                version_number=version_number+1                         #increamenting the version number for the next check
                webbrowser.open(url)                                    #downloading the .zip file
                time.sleep(5)
                os.mkdir(f"C:/Users\{user}/Desktop/PythonBasic/HexFile")
                ExtractZIP()
                Acto_function()
                shutil.rmtree(f"C:/Users\{user}/Desktop/PythonBasic/HexFile")
                break
            else:
                print("File not found")

print("Out of the Function need to restart the setup")


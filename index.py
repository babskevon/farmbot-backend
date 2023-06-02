import serial
import serial.tools.list_ports
from serialMonitor import Command
from get_request import GetRequest
import time
import requests
import sys, os
import random
import uuid
from cameraHnadler import Imager



baseUrl = "http://kevinbabise-001-site1.atempurl.com/"

#initialise serial
sender = Command(serial)
port = '/dev/ttyACM0'
baud_rate = 250000

#camera handler
usb_cam_1 = Imager('http://83.229.82.211:8000')


#data=sender.send('G1 X500 F5000')
#print(data)
#data = sender.mega('AgetData soilMoisture')
#print(data)



      
      
      
      
#response = requests.get(url);
#print(response.text);

#global varriable/configurations

speed=0
steps=0
xTrackLength=10
yTrackLength=5
zTrackLength=10
xPlantingTool=0
yPlantingTool=0
zPlantingTool=0
hPlantingTool=0
xIrrigationTool=0
yIrrigationTool=0
zIrrigationTool=0
hIrrigationTool=0
xSprayingTool=0
ySprayingTool=0
zSprayingTool=0
hSprayingTool=0
xTrayTool=0
yTrayTool=0
zTrayTool=0
hTrayTool=0
xSoilTool=0
ySoilTool=0
zSoilTool=0
hSoilTool=0
xPlantSpacing=2
yPlantSpacing=1
waterPerPlant=0
irrigationInterval=0
thresholdMoisture=0
irrigationTrigger=""
chemicalPerPlant=0
sprayingInterval=0
ratioWater=0
ratioChemical=0
sprayingTrigger=""
bootProgress=0
bootTotal=35
stressPhoto="s.jpg"
diseasePhoto="d.jpg"
stressValue=0
diseaseValue=1
currentLocation="0,0"
atX=0
atY=0
atZ=0
currentToolX=0
currentToolY=0
currentToolZ=0
currentToolH=0
operation=""

def modeManual():
    print("manual")
    data = sender.mega('Amessage mode-manual!')
    print(data)
    data={'message':'mode is now manual'}
    data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
    print(data)
    while True:
        time.sleep(5)
        loadConfigurations()
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=mode")
        if(response.text=="normal"):
            print("automatic")
            data = sender.mega('Amessage mode-auto!')
            print(data)
            data={'message':'mode is now automatic'}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            break

def loadConfigurations():
    try:
        global speed
        global steps
        global xTrackLength
        global yTrackLength
        global zTrackLength
        global xPlantingTool
        global yPlantingTool
        global zPlantingTool
        global hPlantingTool
        global xIrrigationTool
        global yIrrigationTool
        global zIrrigationTool
        global hIrrigationTool
        global xSprayingTool
        global ySprayingTool
        global zSprayingTool
        global hSprayingTool
        global xTrayTool
        global yTrayTool
        global zTrayTool
        global hTrayTool
        global xSoilTool
        global ySoilTool
        global zSoilTool
        global hSoilTool
        global xPlantSpacing
        global yPlantSpacing
        global waterPerPlant
        global irrigationInterval
        global thresholdMoisture
        global irrigationTrigger
        global chemicalPerPlant
        global sprayingInterval
        global ratioWater
        global ratioChemical
        global sprayingTrigger
    
    
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=speed");
        if(speed!=response.text):
            data={'message':'speed has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        speed=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=steps");
        if(steps!=response.text):
            data={'message':'steps has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        steps=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xTrackLength");
        if(xTrackLength!=response.text):
            data={'message':'bed length x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xTrackLength=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=yTrackLength");
        if(yTrackLength!=response.text):
            data={'message':'bed length y has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        yTrackLength=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=zTrackLength");
        if(zTrackLength!=response.text):
            data={'message':'bed length z has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        zTrackLength=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xPlantingTool");
        if(xPlantingTool!=response.text):
            data={'message':'planting tool x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xPlantingTool=response.text
        time.sleep(6)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=yPlantingTool");
        if(yPlantingTool!=response.text):
            data={'message':'planting tool y has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        yPlantingTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=zPlantingTool");
        if(zPlantingTool!=response.text):
            data={'message':'planting tool z has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        zPlantingTool=response.text
        time.sleep(1)
        BootProgress()
        
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=hPlantingTool");
        if(hPlantingTool!=response.text):
            data={'message':'planting tool h has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        hlantingTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xIrrigationTool");
        if(xIrrigationTool!=response.text):
            data={'message':'irrigation tool x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xIrrigationTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=yIrrigationTool");
        if(yIrrigationTool!=response.text):
            data={'message':'irrigation tool y has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        yIrrigationTool=response.text
        time.sleep(1)
        BootProgress()
        
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=zIrrigationTool");
        if(zIrrigationTool!=response.text):
            data={'message':'irrigation tool z has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)

        zIrrigationTool=response.text
        time.sleep(6)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=hIrrigationTool");
        if(hIrrigationTool!=response.text):
            data={'message':'irrigation tool h has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        hIrrigationTool=response.text
        time.sleep(6)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xSprayingTool");
        if(xSprayingTool!=response.text):
            data={'message':'spraying tool x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xSprayingTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=ySprayingTool");
        if(ySprayingTool!=response.text):
            data={'message':'spraying tool y has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        ySprayingTool=response.text
        time.sleep(1)
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=zSprayingTool");
        if(zSprayingTool!=response.text):
            data={'message':'spraying tool z has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        zSprayingTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=hSprayingTool");
        if(hSprayingTool!=response.text):
            data={'message':'spraying tool h has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        hSprayingTool=response.text
        time.sleep(1)
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xTrayTool");
        if(xTrayTool!=response.text):
            data={'message':'tray tool x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xTrayTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=yTrayTool");
        if(yTrayTool!=response.text):
            data={'message':'tray tool y has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        yTrayTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=zTrayTool");
        if(zTrayTool!=response.text):
            data={'message':'tray tool z has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        zTrayTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=hTrayTool");
        if(hTrayTool!=response.text):
            data={'message':'tray tool h has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        hTrayTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xSoilTool");
        if(xSoilTool!=response.text):
            data={'message':'soil tool x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xSoilTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=ySoilTool");
        if(ySoilTool!=response.text):
            data={'message':'soil tool y has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        ySoilTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=zSoilTool");
        if(zSoilTool!=response.text):
            data={'message':'soil tool z has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        zSoilTool=response.text
        time.sleep(6)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=hSoilTool");
        if(hSoilTool!=response.text):
            data={'message':'soil tool h has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        hSoilTool=response.text
        time.sleep(1)
        BootProgress()
        
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=xPlantSpacing");
        if(xPlantSpacing!=response.text):
            data={'message':'plant spacing x has been changed to '+response.text}
            data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
        
        xPlantSpacing=response.text
        time.sleep(1)
        BootProgress()
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=yPlantSpacing");
            if(yPlantSpacing!=response.text):
                data={'message':'plant spacing y has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            yPlantSpacing=response.text
            BootProgress()
            
        
        except:
            print("net error")
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=waterPerPlant");
            if(waterPerPlant!=response.text):
                data={'message':'water per plant has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            waterPerPlant=response.text
            BootProgress()
        
        except:
            print("net error")
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=irrigationInterval");
            if(irrigationInterval!=response.text):
                data={'message':'irrigation interval has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            irrigationInterval=response.text
            BootProgress()
        
        except:
            print("net error")
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=thresholdMoisture");
            if(thresholdMoisture!=response.text):
                data={'message':'threshold moisture has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            thresholdMoisture=response.text
            BootProgress()
        
        except:
            print("net error")
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=irrigationTrigger");
            if(irrigationTrigger!=response.text):
                data={'message':'irrigationTrigger  has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            irrigationTrigger=response.text
            BootProgress()
        
        except:
            print("net error")
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=chemicalPerPlant");
            if(chemicalPerPlant!=response.text):
                data={'message':'plant chemical per plant has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            chemicalPerPlant=response.text
        
        except:
            print("net error")
        
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=sprayingInterval");
            if(sprayingInterval!=response.text):
                data={'message':'spraying interval has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            sprayingInterval=response.text
            BootProgress()
        
        except:
            print("net error")
       
         
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=ratioWater");
            if(ratioWater!=response.text):
                data={'message':'ratio water has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            ratioWater=response.text
            BootProgress()
        except:
            print("net error")
        
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=ratioChemical");
            if(ratioChemical!=response.text):
                data={'message':'ratio chemical has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            
            ratioChemical=response.text
        except:
            print("net error")
        
        
        try:
            response = requests.get(baseUrl+"api/Settings/GetSetting?name=sprayingTrigger");
            if(sprayingTrigger!=response.text):
                data={'message':'spraying trigger has been changed to '+response.text}
                data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
            sprayingTrigger=response.text
        except:
            print("net error")
        
        
        
        
        data = sender.mega('AsetConfig amountOfWaterPerPlant '+waterPerPlant)
        print(data)
        
        data = sender.mega('AsetConfig amountOfChemicalPerPlant '+chemicalPerPlant)
        print(data)
        
        
        print("done loading configuration")
        Message("loading configs Done")
    
    except Exception as e:
        print("ërror occurred during loading of configurations ")
        #Message("ërror occurred during loading of configurations "+e)


def BootProgress():
    global bootProgress
    global bootTotal
    if(bootProgress<=1):
        Screen("pi loading config...")
        Message("pi is loading configurations")
    
    bootParcentage=str(int((bootProgress/bootTotal)*100))+"%";
    Screen("Boot:"+bootParcentage)
    Message("pi boot progress:"+bootParcentage)
    bootProgress+=1
    
        
        

def Message(message):
    data={'message':message}
    data=requests.post(url=baseUrl+"api/Messages/Insert",data=data)
    
        
        
def Screen(message):
    data = sender.mega("Amessage "+message)
    print(data)
        
def events():
    
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=irrigationTest");
    print(response.text)
    if(response.text=="1"):
        irrigationTest()
        
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=sprayingTest");
    print(response.text)
    if(response.text=="1"):
        sprayingTest()
    
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=stressAnnalysisTest");
    print(response.text)
    if(response.text=="1"):
        stressAnnalysisTest()
        
        
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=diseaseAnnalysisTest");
    print(response.text)
    if(response.text=="1"):
        diseaseAnnalysisTest()
        
        
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=spray");
    print(response.text)
    if(response.text=="1"):
        spray()
    
    """"response = requests.get(baseUrl+"api/Settings/GetSetting?name=irrigate");
    print(response.text)
    if(response.text=="1"):
        irrigate()
    
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=plant");
    print(response.text)
    if(response.text=="1"):
        plant()
        
        
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=moveX");
    print(response.text)
    if(response.text!="0"):
        moveX(response.text)
        
    
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=moveY");
    print(response.text)
    if(response.text!="0"):
        moveY(response.text)
        
        
    response = requests.get(baseUrl+"api/Settings/GetSetting?name=moveZ");
    print(response.text)
    if(response.text!="0"):
        moveZ(response.text)"""
        
def Home():
    data=sender.send('G90')
    data=sender.send('G1 X0 Y0 Z0 F'+str(speed))
    
    
def gotoAtPosition():
    data=sender.send('G90')
    data=sender.send('G1 X'+str(atX)+' Y'+str(atY)+' Z'+str(atZ)+' '+'F'+str(speed))
    print(data)



def moveX(value):
    Screen("moving in x ...")
    Message("moving in x")
    data=sender.send('G90')
    data=sender.send('G1 X'+str(value)+' '+'F'+str(speed))
    data={"name": "moveX","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    
    
    
def moveY(value):
    Screen("moving in y...")
    Message("moving in y")
    data=sender.send('G90')
    data=sender.send('G1 Y'+str(value)+' '+'F'+str(speed))
    data={"name": "moveY","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    
    
def moveZ(value):
    Screen("moving in z...")
    Message("moving in z")
    data=sender.send('G90')
    data=sender.send('G1 Z'+str(value)+' '+'F'+str(speed))
    data={"name": "moveZ","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)




def plant():
    global operation
    Screen("planting...")
    Message("planting job started")
    
    setCurrentTool(xPlantingTool,yPlantingTool,zPlantingTool,hPlantingTool)
    operation="planting"
    
    Home()
    gotoTool()
    pickTool()
    traverseLength()
    
    gotoTool()
    releaseTool()
    Home()
    
    
    
    
    
    
    Message("planting  job has ended")
    

        
    data={"name": "plant","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)







def irrigate():
    global operation
    Screen("irrigate")
    Message("irrigation job started")
    
    setCurrentTool(xIrrigationTool,yIrrigationTool,zIrrigationTool,hIrrigationTool)
    operation="irrigation"
    
    Home()
    gotoTool()
    pickTool()
    traverseLength()
    
    gotoTool()
    releaseTool()
    
    
    
    
    
    
    Message("irrigation  job has ended")
    

        
    data={"name": "irrigate","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    
        
        
def spray():
    global operation
    Screen("spraying")
    Message("spraying job started")
    
    setCurrentTool(xSpraying,ySpraying,zSpraying,hSpraying)
    operation="spraying"
    
    #Home()
    #gotoTool()
    #pickTool()
    traverseLength()
    
    #gotoTool()
    #releaseTool()
    
    
    
    
    
    
    Message("spraying job has ended")
    

        
    data={"name": "spray","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    

def camera():
    global stressPhoto
    global diseasePhoto
    
    
def stressModel():
    global stressPhoto
    global diseasePhoto
    global stressValue
    global diseaseValue
    
    data = usb_cam_1.diagonise()
    stressPhoto = data[0]
    diseasePhoto = data[0]
    stressValue = data[1]
    diseaseValue = data[1]
    
    
def diseaseModel():
    global diseaseValue




def stressAnnalysisTest():
    global stressPhoto
    global stressValue
    
    Screen("testing-stress")
    Message("tested stress annalysis")
    
    camera()
    time.sleep(6)
    stressModel()
    diseaseModel
    time.sleep(6)
    
    name = str(uuid.uuid4())
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir,stressPhoto)
    files = {'file': open(filepath, 'rb'), 'fileName':(None, name), 'stress': (None, stressValue), 'disease': (None, diseaseValue), 'location': (None, currentLocation),}
    data={"file": "m.jpg","stress": stressValue,"disease":diseaseValue,"location":"8,9"}
    r = requests.post(url=baseUrl+"api/Photos/UploadFiles", files=files)
    #print(r)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    

        
    data={"name": "stressAnnalysisTest","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)  
    
    
def diseaseAnnalysisTest():
    global stressPhoto
    global stressValue
    
    Screen("testing-disease")
    Message("tested disease annalysis")
    
    camera()
    time.sleep(6)
    stressModel()
    diseaseModel
    time.sleep(6)
    
    name = str(uuid.uuid4())
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir,stressPhoto)
    files = {'file': open(filepath, 'rb'), 'fileName':(None, name), 'stress': (None, stressValue), 'disease': (None, diseaseValue), 'location': (None, currentLocation),}
    data={"file": "m.jpg","stress": stressValue,"disease":diseaseValue,"location":"8,9"}
    r = requests.post(url=baseUrl+"api/Photos/UploadFiles", files=files)
    #print(r)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    

        
    data={"name": "diseaseAnnalysisTest","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)  



def irrigationTest():
    Screen("testing-irrigation")
    Message("tested irrigation mode")
    data = sender.mega('Aoperate irrigation')

        
    data={"name": "irrigationTest","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    
    
    

def sprayingTest():
    Screen("testing-spraying")
    Message("tested spraying mode")
    data = sender.mega('Aoperate spraying')
    
        
    data={"name": "sprayingTest","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    
def positionData():
        data=sender.send('M114')
        time.sleep(1)
        
        try:
            arrData=data.split(" ")
            x=arrData[0].replace("X:","")
            
            
            y=arrData[1].replace("Y:","")
            
            
            z=arrData[2].replace("Z:","")
            
            
            e=arrData[3].replace("E:","")
            
            return x,y,z,e
        
        except:
            return 0,0,0,0
        
        
def updateLocation():
    global currentLocation
    x,y,z,e=positionData()
    currentLocation=str(z)+","+str(y)
    
    
    data={"name": "farmbotPosition","value": currentLocation}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)
    #print(data)


def atPosition():
    global atX, atY, atZ
    x,y,z,e=positionData()
    atX=x
    atY=y
    atZ=z
    
def setCurrentTool(x,y,z,h):
    global currentToolX, currentToolY, currentToolZ, currentToolH
    currentToolX=x
    currentToolY=y
    currentToolZ=z
    currentToolH=h
    
    
def gotoTool():
    data=sender.send('G90')
    data=sender.send('G1 X'+str(currentToolX)+' Y'+str(currentToolY)+' '+'F'+str(speed))
    
    data=sender.send('G1 Z'+str(currentToolZ)+' '+'F'+str(speed))
    
    
    
    print(data)
    

def pickTool():
    data = sender.mega('Aoperate toolMount grab')
    print(data)
    
    

def releaseTool():
    data = sender.mega('Aoperate toolMount release')
    print(data)
    
    
def pickSeed():
    data = sender.mega('Aoperate sunctionPump on')
    print(data)
    
    

def releaseSeed():
    data = sender.mega('Aoperate sunctionPump off')
    print(data)
    

    
def gotoTray():
    data=sender.send('G90')
    data=sender.send('G1 X'+str(xTrayTool)+' Y'+str(yTrayTool)+' '+'F'+str(speed))
    
    data=sender.send('G1 Z'+str(zTrayTool)+' '+'F'+str(speed))
    
    
    
    print(data)
    
    
def spray():
    data = sender.mega('Aoperate spraying')
    print(data)
    
    
    
def irrigate():
    data = sender.mega('Aoperate irrigation')
    print(data)
    
    
    
def sprayingNodeRoutine():
    data=sender.send('G90')
    sender.send('G1 Z'+str(hSprayingTool)+' '+'F'+str(speed))
    spray()
    time.sleep(7)
    sender.send('G1 Z'+str(0)+' '+'F'+str(speed))
    

def irrigationNodeRoutine():
    data=sender.send('G90')
    sender.send('G1 Z'+str(hIrrigationTool)+' '+'F'+str(speed))
    irrigate()
    time.sleep(7)
    sender.send('G1 Z'+str(0)+' '+'F'+str(speed))
    
    


def plantingNodeRoutine():
    data=sender.send('G90')
    sender.send('G1 Z'+str(hPlantingTool)+' '+'F'+str(speed))
    gotoTray()
    pickSeed()
    gotoAtPosition()
    sender.send('G1 Z'+str(hPlantingToolTool)+' '+'F'+str(speed))
    releaseSeed()
    time.sleep(7)
    sender.send('G1 Z'+str(0)+' '+'F'+str(speed))
    

    

def  traverseWidth():
    data=sender.send('G90')
    sender.send('G1 Y'+str(0)+' '+'F'+str(speed))
    while float(atY)<float(yTrackLength):
        print("-------")
        print(atY)
       
        data=sender.send('G91')
        data=sender.send('G1 Y'+str(yPlantSpacing)+' '+'F'+str(speed))
        atPosition()
        updateLocation()
        
        if operation=="spraying":
            sprayingNodeRoutine()
            
        if operation=="irrigation":
            irrigationNodeRoutine()
            
        if operation=="irrigation":
            plantingNodeRoutine()
        
        
        
        
        
def traverseLength():
    data=sender.send('G90')
    sender.send('G1 Z'+str(0)+' '+'F'+str(speed))
    while float(atZ)< float(xTrackLength):
        data=sender.send('M121')
        print("###############")
        print(atZ)
        traverseWidth()
        print("###############")
        
        atPosition()
        data=sender.send('G91')
        data=sender.send('G1 Z'+str(xPlantSpacing)+' '+'F'+str(speed))
       
        
    

        
def spray():
    Screen("spraying")
    Message("spraying job started")
    
    setCurrentTool(xSprayingTool,ySprayingTool,zSprayingTool,hSprayingTool)
    Home()
    
    Message("spraying job has ended")

        
    data={"name": "spray","value": "0"}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.put(url=baseUrl+"api/Settings/UpdateSetting",json=data,headers=headers)    


def data():
    soilMoisture = sender.mega('AgetData soilMoisture')
    sender.mega('ok')
    time.sleep(1)
    humidity = sender.mega('AgetData humidity')
    sender.mega('ok')
    time.sleep(1)
    lightIntensity = sender.mega('AgetData lightIntensity')
    sender.mega('ok')
    time.sleep('ok')
    temperature = sender.mega('AgetData temperature')
    sender.mega('ok')
    
    
    data={"name": "soilMoisture","reading": soilMoisture}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.post(url=baseUrl+"api/Instruments/Insert",json=data,headers=headers) 
    print(data)
    
    data={"name": "humidity","reading": humidity}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.post(url=baseUrl+"api/Instruments/Insert",json=data,headers=headers) 
    print(data)
    
    data={"name": "lightIntensity","reading":lightIntensity}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.post(url=baseUrl+"api/Instruments/Insert",json=data,headers=headers) 
    print(data)
    
    data={"name": "temperature","reading":temperature}
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    data=requests.post(url=baseUrl+"api/Instruments/Insert",data=data,headers=headers) 
    print(data)
    
        
loadConfigurations()

traverseLength()

#while True:
    #traverseLength()
    #Message("waiting to sync with peripheral firmware")
    #data = sender.mega('AgetData soilMoisture')
    #print(data)
    #if data=="Ready":
        #Message("success firmware is in sync")
        #break
    
Message("waiting to sync with peripheral firmware")
time.sleep(6)
Message("success firmware in sync")


    
    


    


while True:
    try:
        time.sleep(5)
        events()
        response = requests.get(baseUrl+"api/Settings/GetSetting?name=mode");
        if(response.text=="manual"):
            modeManual()
    except Exception as e:
        print(e)
        #Message("error "+str(e))
   
        
    

    
    
   

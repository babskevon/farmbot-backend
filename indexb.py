import serial
import serial.tools.list_ports
from serialMonitor import Command
from get_request import GetRequest
import time
#from photo_disease import photo_disease
#import cv2
url = "https://my.api.mockaroo.com/Users.json?key=a8eb8890"

#initialise serial
sender = Command(serial)
manager = GetRequest(sender,url)

#photo = photo_disease()



port = '/dev/ttyACM0'
baud_rate = 250000

#kkk = True
sender.send('G90')
time.sleep(4)
#sender.send('G92 X0 Y0 E0 Z0')
#time.sleep(1)
while True:
    #manager.sensorData()
    #print(manager.data)
    #manager.receive()
    #sender.send("M667")
    #sender.send("M114")
    sender.send('G1 Z1000 F50')
    #time.sleep(2)
    sender.send("M114")
    #time.sleep(2)
    sender.send('G1 X1000 F50')
    #time.sleep(1)
    sender.send('M114')
    
    #sender.send('G1 X0 F100')
    #time.sleep(1)
    #data = sender.mega('AgetData soilMoisture')
    #print(data)
    #time.sleep(2)
    
    
    #break


#with serial.Serial(port,baud_rate,timeout=1) as sender:
 #   time.sleep(0.1)
 #   if sender.isOpen():
  #      print("{} connected".format(sender.port))
   #     sender.readlines()
    #    time.sleep(5)
     #   sender.write("G1 X500 F100000\n".encode())
      #  print(sender.readline())
       # time.sleep(2)
        #sender.write("G1 X200 F10000\n".encode())
        #while sender.inWaiting() == 0: pass
        #if sender.inWaiting()>0:
         #   response = sender.readline()
          #  print(response)
           # sender.flush()

#ports = serial.tools.list_ports.comports()

#for port,desc, hwid in sorted(ports):
#    print("{}:{} [{}]".format(port,desc,hwid))

#time.sleep(10)



#print("Serial starting....")

#sender.write('M114\n'.encode())
#time.sleep(1)

#response = sender.readline()
#sender.write(b'M2')
#time.sleep(3)
#print("move to next position")
#print(response)
#sender.write(b'G01 X7000 Y3000 Z10 F1000\n')
#response = sender.readline()
#time.sleep(2)
#print(response)


#sender.close()

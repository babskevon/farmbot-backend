import time
from format_gcode import g_code
import cv2

port = '/dev/ttyACM0'
baud_rate = 250000

port2 = '/dev/ttyUSB0'
baud_rate2 = 9600


class Command:
    def __init__(self,serial):
        self.sender = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(5)
        
        self.isOpen = self.sender.isOpen
        while self.isOpen == False:
            self.sender = serial.Serial(port, baud_rate,timeout=1)
            print("connecting...")
        else:
            print("{}-Ramps is now connected".format(self.sender.port))
            self.sender.readlines()
            
        self.sender2 = serial.Serial(port2, baud_rate2, timeout=1)
        self.isOpen2 = self.sender2.isOpen
        
        while self.isOpen2 == False:
            self.sender2 = serial.Serial(port2, baud_rate2, timeout = 1)
            print("connecting...")
        else:
            print("{}-Mega is now connected".format(port2))
            self.sender2.readlines()
            
    def mega(self,code):
        command = g_code(code)
        if self.sender2.isOpen():
            self.sender2.write(command.encode())
            data = self.sender2.readline().decode().strip()
            self.sender2.flushInput()
            time.sleep(0.5)
            return data
    def send2(self,code):
        print(code)
        command = g_code(code)
        if self.sender.isOpen():
            self.sender.write(command.encode())
            data = self.sender.readline().decode().strip()
            print(data)
            self.sender.flushInput()
            time.sleep(1)
            return data
        else:
            print("No commands received")
            
    def send(self,code):
        print(code)
        command = g_code(code)
        if self.sender.isOpen():
            self.sender.write(command.encode())
            time.sleep(4)
            
            data = self.sender.readline().decode().strip()
            while "busy: processing" in data:
                print("busy.....")
                time.sleep(0.5)
                self.sender.write(command.encode())
                time.sleep(2)
                data = self.sender.readline().decode().strip()
            else:
                print(code)
                
            #if "busy: processing" in data:
                #print("busy......")
                #print("trying to restart job: {}".format(code))
                #self.sender.write(command.encode())
                #time.sleep(6)
                #data = self.sender.readline().decode().strip()
            if(data == "ok"):
                print("Executing {}...".format(code))
            else:
                print(data)
            self.sender.flushInput()
            time.sleep(0.5)
            return data
            
            
        
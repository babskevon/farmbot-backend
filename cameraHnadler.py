import subprocess
import datetime
import requests
import json

class Imager:
    def __init__(self,url):
        self.url = url
    def capture_photo(self):
        current_date = datetime.datetime.now()
        filename = current_date.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
        path = "images/"+filename
        command = ['fswebcam',path]
        subprocess.run(command)
        return [path,filename]
    
    def growth(self):
        url = self.url + '/photo2/'
        path = self.capture_photo()[0]
        file = open(path,'rb')
        response = requests.post(url,files={'name':file})
        result = [path,response.text]
        print(result)
        return result
    
    def diagonise(self):
        url = self.url + '/photo/'
        #print(url)
        path = self.capture_photo()[0]
        file = open(path,'rb')
        response = requests.post(url,files={'name':file})
        result = [path,response.text]
        #print(result)
        return result
    
    
#one = Imager('http://83.229.82.211:8000')
#one.diagonise()
#one.growth()
        
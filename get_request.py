import requests
import json
import time

class GetRequest:
    data = {}
    def __init__(self,sender=None,url=None):
        self.base_url = url
        self.sender = sender
        self.jobs = []
        self.job_id = ''
        
    def sensorData(self):
        rec = self.sender.mega("AgetData soilMoisture")
        time.sleep(1)
        GetRequest.data['moisture'] = rec
        GetRequest.data['humidity'] = self.sender.mega("AgetData humidity")
        time.sleep(1)
        GetRequest.data['temperature'] = self.sender.mega("AgetData temperature")
        time.sleep(1)
        GetRequest.data["lightIntensity"] = self.sender.mega("AgetData lightIntensity")
        time.sleep(1)
        
    def test(self):
        response = requests.get(self.base_url)
        for ddd in json.loads(response.text):
            print(b"{}".format(ddd['last_name']))
        #print(json.loads(response.text))
        
    
    def receive(self,data=None):
        if data is not None:
            self.base_url += data
        response = requests.get(self.base_url)
        if(response.status_code == 200):
            response = json.loads(response.text)
            print(response)
            self.job_id = response['job_id']
            self.jobs = response['gcodes']
            return True
        else:
            return False
    
    def execute(self):
        for job in self.jobs:
            if job.startswith("A"):
                data = self.sender.mega(job)
            else:
                data = self.sender.send(job)
        
            
            

        
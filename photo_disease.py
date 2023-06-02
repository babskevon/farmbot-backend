from picamera import PiCamera
from time import sleep,time
import requests
import pygame
import pygame.camera


def test_pygame():
    pygame.init()
    pygame.camera.init()
    camera_list = pygame.camera.list_cameras()
    print("here now",camera_list)
    if not camera_list:
        print("No cameras")
        pygame.quit()
        
    camera = pygame.camera.Camera(camera_list[0],(640,480))
    camera.start()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Usb cam")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                image = camera.get_image()
                pygame.image.save(image,"photo.jpg")
                print("photo save successfully")
test_pygame()
def photo_disease():
    camera = PiCamera()
    camera.start_preview()
    name = str(int(time())) + ".jpg"
    camera.capture(name)
    sleep(2)
    camera.stop_preview()
    return name



def take_photo(upload_url,disease_url):
    name = photo_disease()
    file = open(name,'rb')
    response = requests.post(disease_url,files={'name':file})
    server_upload = requests.post(upload_url,data=response.text,files={'fileName':file})
    
    


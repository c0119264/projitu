from picamera import PiCamera
from time import sleep
from datetime import datetime




camera=PiCamera()
camera.start_preview()
sleep(5)
filename=datetime.now().strftime("%Y-%m-%dT%H%M%S")+".png"
camera.capture("~/projitu/filename")
camera.stop_preview()

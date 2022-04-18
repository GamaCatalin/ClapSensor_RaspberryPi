import RPi.GPIO as GPIO
import time
from time import sleep

soundChannel = 21
ledChannel = 20


GPIO.setmode(GPIO.BCM)
GPIO.setup(soundChannel, GPIO.IN)
GPIO.setup(ledChannel, GPIO.OUT)


ch_flag = False

def callback(soundChannel):
    global ch_flag
    if GPIO.input(soundChannel):
        print("Sound Detected!")
        ch_flag = (not ch_flag)
        GPIO.output(ledChannel, ch_flag)
        sleep(0.5)
        
        #GPIO.output(ledChannel, GPIO.HIGH)
        #sleep(0.1)
        #GPIO.output(ledChannel, GPIO.LOW)
        #sleep(0.1)
    else:       
        print("SoundDetected!")
       
       
GPIO.add_event_detect(soundChannel, GPIO.BOTH, bouncetime=600)
GPIO.add_event_callback(soundChannel, callback)
       
while True:
       time.sleep(1)
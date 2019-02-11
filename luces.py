import RPi.GPIO as gpio           
from time import sleep


led1=23

gpio.setmode(gpio.BCM)

gpio.setup(led1,gpio.OUT)

def luzPrendida():
    gpio.output(led1,True)

def luzApagada():
    gpio.output(led1,False)
    

while True:
    gpio.output(led1,True)
    print ("apagado")
    sleep(1)
    gpio.output(led1,False)
    print ("encendido")
    sleep(1)

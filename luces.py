import RPi.GPIO as gpio

led1=23
venti=24

gpio.setmode(gpio.BCM)

gpio.setup(led1,gpio.OUT)
gpio.setup(venti,gpio.OUT)

def luzPrendida():
    gpio.output(led1,True)

def luzApagada():
    gpio.output(led1,False)

def ventiPrendido():
    gpio.output(venti,True)

def ventiApagado():
    gpio.output(venti,False)

# while True:
#     gpio.output(led1,True)
#     print ("apagado")
#     sleep(1)
#     gpio.output(led1,False)
#     print ("encendido")
#     sleep(1)

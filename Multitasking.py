from usched import Sched
from machine import Pin
from time import sleep
led1 = Pin(5, Pin.OUT)
led2 = Pin(4, Pin.OUT)

def toggle1(objLED):
    while True:
        objLED.value(not objLED.value())
        yield 1

def toggle1(objLED):
    while True:
        objLED.value(not objLED.value())
        yield .1

objSched = Sched()
objSched.add_thread(toggle1(led1))
objSched.add_thread(toggle1(led2))
objSched.run()

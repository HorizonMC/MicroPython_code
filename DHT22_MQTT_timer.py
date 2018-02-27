#hardware platform: FireBeetle-ESP8266
import network
from mqtt import MQTTClient 
from machine import Pin,Timer
import dht
import time

pin  = Pin(12)
sensor = dht.DHT22(pin)

led=Pin(2,Pin.OUT)
tim = Timer(1)
tim1 = Timer(2)


def sub_cb(topic, msg): 
   print(msg) 

def blink(t):
  led.value(not led.value())

def Print(t):
  print ("test")

client = MQTTClient("ESP_Wemos", "m12.cloudmqtt.com",user="wbpgeuzw", password="ClkZVjUA5HKw", port=17441)
client.set_callback(sub_cb) 
client.connect()

tim.init(period=1000,mode=Timer.PERIODIC, callback=blink)
tim1.init(period=2000,mode=Timer.PERIODIC, callback=Print)

try:
  while True:
    pass
except:
  tim.deinit()
  tim1.deinit()

import network
from mqtt import MQTTClient 
from machine import Pin
import dht
import time
##Config
pin  = Pin(12)
sensor = dht.DHT22(pin)

def sub_cb(topic, msg): 
   print(msg) 

def DHT_Pub(t):
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    print("Temp,Humi : {} C,{} %".format(t,h))
    msg = 'temp:{:.2f},humd:{:.2f}'.format(t,h)
    client.publish(topic="DHT22/feeds/temp",msg=msg)
    #client.publish(topic="DHT22/feeds/Humid",msg=h
    #time.sleep_ms(2000)
# wlan = network.WLAN(network.STA_IF)
# #disable AP Mode
# wlan.active(False)
# #enable STA Mode
# wlan.active(True)
# wlan.connect("Horizon_Plus","1212312121")

# while not wlan.isconnected():  
#     machine.idle() 
# print("Connected to Wifi\n") 

client = MQTTClient("ESP_Wemos", "m12.cloudmqtt.com",user="wbpgeuzw", password="ClkZVjUA5HKw", port=17441)
client.set_callback(sub_cb) 
client.connect()

tim.init(period=2000,mode=Timer.PERIODIC, callback=blink)
tim1.init(period=1000,mode=Timer.PERIODIC, callback=DHT_Pub)

#for i in range(10):
try:
    while True:
        
except:        
    tim.deinit()
    tim1.deinit()
finally :
    client.disconnect()
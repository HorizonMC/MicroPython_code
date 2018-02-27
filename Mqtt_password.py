import network
from mqtt import MQTTClient 
import machine 
import time 
 
def sub_cb(topic, msg): 
   print(msg) 
 
wlan = network.WLAN(network.STA_IF)
#disable AP Mode
wlan.active(False)
#enable STA Mode
wlan.active(True)
wlan.connect("Horizon_Plus","1212312121")
#wlan.connect("TheHorizon","0887571899") 
 
while not wlan.isconnected():  
    machine.idle() 
print("Connected to Wifi\n") 
 
client = MQTTClient("ESP_Wemos", "m12.cloudmqtt.com",user="wbpgeuzw", password="ClkZVjUA5HKw", port=17441) 
client.set_callback(sub_cb) 
client.connect()
#client.subscribe(topic="youraccount/feeds/lights",qos=0) 
while True:
    print("Sending ON")
    client.publish(topic="youraccount/feeds/lights", msg="ON")
    time.sleep(2)
    print("Sending OFF")
    client.publish(topic="youraccount/feeds/lights", msg="OFF")
    #client.disconnect();
    time.sleep(2)
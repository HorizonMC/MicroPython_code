from machine import Pin
import dht
import time


pin  = Pin(12)
sensor = dht.DHT22(pin)


#for i in range(10):
while True:
	sensor.measure()
	t = str(sensor.temperature())
	h = str(sensor.humidity())
	print("Temp,Humi : {} C,{} %".format(t,h))
	time.sleep_ms(500)

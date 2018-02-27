import time
print('Hello world! I can count:')
i = 1
 
#while True:
for i in range(10):
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    print("Wellcome TO ESP8266 Micropython")
    print("Wait .....")
    print(i)
    i += 1
    time.sleep(1.0)  # Delay for 1 second.
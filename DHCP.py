import network
# create network instances
sta_if = network.WLAN(network.STA_IF)

# ap_if = network.WLAN(network.AP_IF)
#disable AP Mode
#ap_if.active(False)
#enable STA Mode
sta_if.active(True)
#connect to router
#sta_if.connect("TOPIC_IOT_DEV","1212312121")
# sta_if.connect("TheHorizon","0887571899")
sta_if.connect("Horizon_Plus","1212312121")
#sta_if.connect("Horizon_PC","1212312121")
#sta_if.connect("Anuchit","0818037803")
#check result
print(sta_if.isconnected())
print(sta_if.ifconfig())
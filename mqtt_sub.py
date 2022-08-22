
from brachiograph import BrachioGraph

import paho.mqtt.client as mqttClient
import time




bg = BrachioGraph(
    servo_1_parked_pw=1570,
    servo_2_parked_pw=1450,
)

  


def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")
  
def on_message(client, userdata, message):
    print("Message received:"  + str(message.payload))
    heartBeatValue = int(bytes.decode(message.payload)) +1000

    if heartBeatValue <  140 :
        bg.box(bounds=[-2, 7, 2, 11])
        print("drucken")
   

  
Connected = False   #global variable for the state of the connection
broker_address= "mqtt.eclipseprojects.io"
port = 1883
user = "Galaxy"
password = "OrionBetaAlpha72"


client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("coco/heart")
  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
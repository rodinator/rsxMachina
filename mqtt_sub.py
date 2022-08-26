
from turtle import delay
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

heartBeatAverage = 0 
counter = 0
def on_message(client, userdata, message):
    global heartBeatAverage,heartBeatValue, counter
    print("Message received:"  + str(message.payload))
    heartBeatValue = int(bytes.decode(message.payload))
    heartBeatAverage = heartBeatValue + heartBeatAverage
    counter += 1
    print(heartBeatAverage / counter)
    print("Counter: " + str(counter))
    print("add heartbeat to Average, the new Average is: " + str(heartBeatAverage/counter))
    if counter == 20 :
        heartBeatAverage = heartBeatAverage / counter
        print("print started with the Average of" + str(heartBeatAverage) )
        bg.box(bounds=[-2,4,2+0.00375094*heartBeatAverage,8+0.00375094*heartBeatAverage])
        print("print finished")
        heartBeatAverage = 0
        counter = 0

        
    
    #if heartBeatValue ==  140 :
        
   

  
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
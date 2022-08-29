var mqtt;                           // MQTT variable/object
var reconnectTimeout = 5000;        // 5 seconds for the reconnectTimeout
var host="mqtt.eclipseprojects.io";               // MQTT bridge IP
var port=1883;                      // MQTT bridge port 
MQTTconnect();                      // Initialise the MQTT connections

function MQTTconnect(){
  console.log("mqtt connecting to " + host + ":" + port);
  mqtt = new Paho.MQTT.Client(host, port, "client_test");
  var options = {
    timeout: 100,
    onSuccess: onConnect,
    onFailure: onFailure,
  };
  mqtt.onMessageArrived = onMessageArrived;
  mqtt.connect(options); // connect
}

function onConnect(){
  console.log("Mqtt Connected - Subscribe to the topics");
  mqtt.subscribe("coco/heart");
}
            
function onFailure(message){
  console.log("Connection attempt to MQTT " + host + " failed");
  setTimeout(MQTTconnect, reconnectTimeout);
}

function onMessageArrived(msg){
   msg.destinationName == "coco/heart"
    console.log("coco/heart: ", msg.payloadString);
  

}
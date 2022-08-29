let pahoConfig = {
    hostname: "mqtt.eclipseprojects.io",  //The hostname is the url, under which your FROST-Server resides.
    port: "80",           //The port number is the WebSocket-Port,
                            // not (!) the MQTT-Port. This is a Paho characteristic.
    clientId: "123nasdj123" + Math.random().toString(16).substr(2, 8)  //Should be unique for every of your client connections.
}

client = new Paho.MQTT.Client(pahoConfig.hostname, Number(pahoConfig.port), pahoConfig.clientId);
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({
onSuccess: onConnect
});

function onConnect() {
// Once a connection has been made, make a subscription and send a message.
console.log("Connected with Server");
client.subscribe("coco/heart");
}

function onConnectionLost(responseObject) {
if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:" + responseObject.errorMessage);
}
}
function onMessageArrived(message) {
console.log("onMessageArrived:" + message.payloadString);
let j = JSON.parse(message.payloadString);
document.getElementById("heartbeat").innerHTML = message.payloadString;
}


from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt
import random, threading, json
from flask_mqtt import Mqtt

#setting mqttnya dulu
mqtt_username = "mqtt"
mqtt_password = "mqtt"
MQTT_Broker = "mqtt.danova.id"
MQTT_Port = 1883
#Keep_Alive_Interval = 60
MQTT_Topic_control = "smartpju/led"pyt
#from gpiozero import LEDssss
# mqtt = Mqtt(app)


mqttc = mqtt.Client()
led_state = False;
led_on = "1"
led_off = "0"

def on_connect(client, userdata, rc):
    mqttc.subscribe(MQTT_Topic_control)

def on_publish(client, userdata, mid):
    	pass

def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass

def on_message(client, userdata, msg):
    data = msg.payload
    baru = data.decode()


mqttc.username_pw_set(mqtt_username, mqtt_password)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port))

def publish_To_control(topic, message):
    mqttc.publish(topic,message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(MQTT_Topic_control))
    print("")   

@app.route('/')
def index():
    return render_template('index.html')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe()

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

@app.route('/led', methods=['POST'])
def onoff():

    global led_state
    if led_state == False:
        nyala = int(led_off)
        led_state = not led_state
        publish_To_control (MQTT_Topic_control, nyala)
        return jsonify( status = payload )
    else:
        mati = int(led_on)
        led_state = not led_state
        publish_To_control (MQTT_Topic_control, mati)
        return jsonify(status = payload)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

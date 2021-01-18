#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

global done_led_status
global cycle_done
global not_done_message_sent
global done_message_sent
global mqttClient
clientName = "WasherMon"
serverAddress = "10.0.0.16"
port = 1883

def on_publish(client,userdata,result):             #create function for callback
#    print("data published \n")
    pass

def connectionStatus(client, userdata, flags, rc):
    mqttClient.subscribe("Basement/Washer/Done")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')

#    print("Yeppers")

DO = 17
GPIO.setmode(GPIO.BCM)

def setup():
    global mqttClient
    global not_done_message_sent
    global done_message_sent
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)
    cycle_done = 0
    done_led_status = 255
    not_done_message_sent = 0
    done_message_sent = 0
    mqttClient = mqtt.Client(clientName)
    mqttClient.on_connect = connectionStatus
    mqttClient.on_message = messageDecoder
    mqttClient.on_publish = on_publish                         
    mqttClient.connect(serverAddress,port)
    ret=mqttClient.publish("Basement/Washer/Done","0")

def in_progress():
#    print 'Cycle In Progress'

def loop():
    global mqttClient
    global not_done_message_sent
    global done_message_sent
    status = 1
    while True:
        done_led_status = ADC.read(0)
    #    done_led_status = 200
        if done_led_status > 220:
           # print 'Not Done, Value = ', done_led_status
            if(not_done_message_sent == 0):
                ret=mqttClient.publish("Basement/Washer/Done","0")
                not_done_message_sent = 0
            cycle_done = 0
            done_message_sent = 0
        else:
           # print 'Done!'
            cycle_done = 1

            if (cycle_done == 1) and (done_message_sent == 0):
                # Send message
                ret=mqttClient.publish("Basement/Washer/Done","1")
                done_message_sent = 0
           #     print 'Message Sent!'
            not_done_message_sent = 0
        time.sleep(5)


if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	

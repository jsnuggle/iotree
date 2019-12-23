"""
Client convenience wrapper for Adafruit IO communication using MQTTClient

For complete details see: https://github.com/adafruit/Adafruit_IO_Python

requires: Adafruit_IO
"""
import sys
from secrets import ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY
from Adafruit_IO import MQTTClient

# MQTT Callback functions:

class AFIOClient :

    def __init__(self, onConnect, onMessage, onDisconnect):
        # Create an MQTT client instance.
        mqttClient = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

        # Setup the callback functions defined above.
        mqttClient.on_connect = onConnect
        mqttClient.on_disconnect = onDisconnect
        mqttClient.on_message    = onMessage

        self.mqttClient = mqttClient

    def connect(self):
        self.mqttClient.connect()

    # Listen on the main thread - process blocking
    def listen(self):
        self.mqttClient.loop_blocking()

    # Listen in the background -- don't block the main loop
    def listen_background(self):
        self.mqttClient.loop_background()


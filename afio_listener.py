#todo: move to config file

from Adafruit_IO import MQTTClient

import sys
from secrets import ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY
from Adafruit_IO import MQTTClient

#todo: move these callbacks out of this file

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

    def listen(self):
        self.mqttClient.loop_blocking()

# Connect to the Adafruit IO server.
#client.connect()

# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.
#client.loop_blocking()

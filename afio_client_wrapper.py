"""
Client convenience wrapper for Adafruit IO communication using MQTTClient

For complete details see: https://github.com/adafruit/Adafruit_IO_Python

requires: Adafruit_IO
"""
import sys
from Adafruit_IO import Client, MQTTClient

# MQTT Callback functions:

class AFIOClient :

    def __init__(self, aio_username, aio_api_key):
        self.client = Client(aio_username, aio_api_key)
        self.mqttClient = MQTTClient(aio_username, aio_api_key)

    def pubsub_feed_listen(self, onConnect, onMessage, onDisconnect):

        # Setup the callback functions defined above.
        self.mqttClient.on_connect    = onConnect
        self.mqttClient.on_disconnect = onDisconnect
        self.mqttClient.on_message    = onMessage
        self.mqttClient.connect()
        self.mqttClient.loop_blocking()

    def publish_status(self, feed_key, status):
        self.client.send_data(feed_key, status)

    # Listen in the background -- don't block the main loop
    def listen_background(self):
        self.mqttClient.loop_background()


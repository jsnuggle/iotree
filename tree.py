"""
Main program

Here we set up a listener on an Adafruit IO channel in order to
capture commands for chrismas tree lights. Lights basic LED
with 3-channel switcher (white, colored, alternating).



"""
import lights
import json
from config import ADAFRUITIO_COMMAND_FEED_KEY, ADAFRUITIO_STATUS_FEED_KEY
from afio_client_wrapper import AFIOClient
from secrets import ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY

print("Welcome to Christmas!")

lights.control.power_on()
aio_client = AFIOClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def onMessage(client, feed_id, payload):
    # Listener for messages from Adafruit IO Feed

    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    executeCommand(json.loads(payload.lower().strip()))

def executeCommand(command):
    """
    Execute a command received from Adafruit IO channel.
    Expected command payload is JSON in the following format:
    {"execute": <command>,"arg": <optional arguments>}

    Supported Commands:
    ------------------
    * color_change: (white|color|party)
    * power: (on|off)
    """
    directive = command['execute'].strip()
    arg = command['arg'].strip() if 'arg' in command else None

    if (directive == 'color_change'):
        print("Set color: {0}".format(arg))
        lights.control.activate_channel(arg)
    elif (directive == 'power'):
        # Google has touble parsing out 'the' when you say Turn off the tree
        arg = arg.replace('the','').strip()
        print("Set power: {0}".format(arg))
        if (arg == 'on'):
            lights.control.power_on()
        else:
            lights.control.power_off()
    elif (directive == 'get_status'):
        status_str = lights.control.get_status()
        print("Get status: %s" % status_str)
        aio_client.publish_status(ADAFRUITIO_STATUS_FEED_KEY, status_str)
    else:
        print('Invalid directive:\'{0}\''.format(directive))

def onConnect(client):
    # Function called when Adafruit IO connection is established
    print('Listening for \'{0}\' changes...'.format(ADAFRUITIO_COMMAND_FEED_KEY))
    client.subscribe(ADAFRUITIO_COMMAND_FEED_KEY)

def onDisconnect(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

aio_client.pubsub_feed_listen(onConnect, onMessage, onDisconnect)

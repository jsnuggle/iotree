import lights
from afio_listener import AFIOClient

FEED_ID = 'google-assistant'

print("Welcome to Christmas!")

lights.control.activate_channel("white")

def onMessage(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    lights.control.activate_channel(payload.lower().strip())

def onConnect(client):
    print('Listening for \'{0}\' changes...'.format(FEED_ID))
    client.subscribe(FEED_ID)

def onDisconnect(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)


afio = AFIOClient(onConnect, onMessage, onDisconnect)
afio.connect()
afio.listen()

#afio.listen_background()
#lights.control.listen_for_button()


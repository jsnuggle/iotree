"""
Lights utility -- interfaces with christmas light channels via GPIO

requires: Adafruit Blinky (board, digitalio)
"""
import board
import digitalio

class Lights:

    def __init__(self):
        self.__initOutputs()
        self.__initInputs()
        self.default_channel_name = 'white'
        self.activeChannel = None

    def initOutputs(self):
        # Initialize the output pins. We use pins 23-25
        outputWhite = digitalio.DigitalInOut(board.D23)
        outputWhite.direction = digitalio.Direction.OUTPUT

        outputColor = digitalio.DigitalInOut(board.D24)
        outputColor.direction = digitalio.Direction.OUTPUT

        outputChange = digitalio.DigitalInOut(board.D25)
        outputChange.direction = digitalio.Direction.OUTPUT

        self.outputs = {
            'white': outputWhite,
            'color': outputColor,
            'party': outputChange
        }

    def deactivateAll(self):
        # deactivate all channels
        for o in self.outputs.values():
            o.value = False

    def activate_channel(self, channel):
        """
        Activate a particular lighting channel. 
        channel: string, one of the three values defined above in initOutputs 
        (white|color|party)
        """
        if channel not in self.outputs:
            print("invalid channel selected ({}) -- please try again".format(channel))
            return

        self.activeChannel = self.outputs.get(channel)
        self.deactivateAll()
        print('turning on {} channel'.format(channel))
        self.activeChannel.value = True

    def power_on(self):
        """
        Power on the lights to the last active channel. If no activeChannel
        is present, select the default
        """
        if self.activeChannel is None:
            self.activeChannel = self.outputs.get(self.default_channel_name)

        self.activeChannel.value = True

    def power_off(self):
        # Power off the lights
        self.deactivateAll()

    __initOutputs = initOutputs
    __initInputs = initInputs

control = Lights()

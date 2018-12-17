import board
import digitalio

class Lights:

    def __init__(self):
        self.__initOutputs()
        self.__initInputs()


    def initOutputs(self):

        outputWhite = digitalio.DigitalInOut(board.D23)
        outputWhite.direction = digitalio.Direction.OUTPUT

        outputColor = digitalio.DigitalInOut(board.D24)
        outputColor.direction = digitalio.Direction.OUTPUT

        outputChange = digitalio.DigitalInOut(board.D25)
        outputChange.direction = digitalio.Direction.OUTPUT

        self.outputs = {
            'white': outputWhite,
            'color': outputColor,
            'change': outputChange
        }

    def initInputs(self):
        button = digitalio.DigitalInOut(board.D4)
        button.direction = digitalio.Direction.INPUT
        button.pull = digitalio.Pull.UP

        self.button = button

    def activateChannel(self, channel):
        #todo: add bounds check
        self.activeChannel = self.outputs.get(channel)
        self.deactivateAll()
        print('turning on {} channel'.format(channel))
        self.activeChannel.value = True

    def deactivateAll(self):
        for o in self.outputs.values():
            o.value = False

    __initOutputs = initOutputs
    __initInputs = initInputs

lights = Lights()

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
            'party': outputChange
        }

    def initInputs(self):
        button = digitalio.DigitalInOut(board.D4)
        button.direction = digitalio.Direction.INPUT
        button.pull = digitalio.Pull.DOWN

        self.button = button

    def activate_channel(self, channel):
        if channel not in self.outputs:
            print("invalid channel selected ({}) -- please try again".format(channel))
            return

        self.activeChannel = self.outputs.get(channel)
        self.deactivate_all()
        print('turning on {} channel'.format(channel))
        self.activeChannel.value = True

    def deactivate_all(self):
        for o in self.outputs.values():
            o.value = False

    __initOutputs = initOutputs
    __initInputs = initInputs

    def listen_for_button(self): 
        while True: 
            if self.button.value: 
                print("button pressed")

control = Lights()

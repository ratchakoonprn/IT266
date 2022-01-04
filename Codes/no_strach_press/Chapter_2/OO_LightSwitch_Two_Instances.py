# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
         self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)
    
# Main code
oLightSwitch1 = LightSwitch()  # create a LightSwitch object
oLightSwitch2 = LightSwitch()  # create another LightSwitch object

#  Test code
oLightSwitch1.show() #False
oLightSwitch2.show() #False
oLightSwitch1.turnOn() # True Turn switch 1 on 
# Switch 2 should be off at start, but this makes it clearer
oLightSwitch2.turnOff()  #True
oLightSwitch1.show() #True
oLightSwitch2.show() #False
print(type(oLightSwitch1))

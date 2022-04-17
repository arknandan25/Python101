from abc import ABC, abstractmethod


class Switchable(ABC):
    """
    Abstract class/Interface

    We cannot create instances of this class
    It only defines how a switchable should function

    This interface makes it easier for us to change our code in the future as any change in a Switchable will not affect
    how any consumer like ElectricPowerSwitch uses it. For ElectricPowerSwitch the usage is defined by this interface
    when it specifies that a Switchable will have a turn_on and off method that a consumer can use.

    LightBulb is a type of Switchable
    Fan is a type of Switchable
    """
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:

    def __init__(self, l: Switchable):
        self.switchable = l
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True


l = LightBulb()
f = Fan()

# Light bulb
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

# Fan
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()

# LightBulb: turned on...
# LightBulb: turned off...
# Fan: turned on...
# Fan: turned off...

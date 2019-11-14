import pigpio
from time import sleep
from PigpioStepperMotor import StepperMotor, fullStepSequence

class Runner:
    def __init__(self, bd, config):
        pi = pi = pigpio.pi()
        self.motor = StepperMotor(pi, *config['pins'], sequence = fullStepSequence)
        self.bd = bd
        self.allowed = False
        self.allowed_mac_addresses = config.get('allowed_mac_addresses', [])
        self.nb_steps = config.get('nb_steps', 2048)
        self.wait_time = config.get('wait_time', 1)

    def rotate(self, arg):
        if (not self.allowed):
            print('Not allowed to run the motor')
            return

        for i in range(self.nb_steps):
            self.motor.rotateClockwise()

        sleep(self.wait_time)

        for i in range(self.nb_steps):
            self.motor.rotateCounterClockwise()

    def check_mac_addresses(self, arg):
        if (self.allowed_mac_addresses == []):
            self.allowed =  True
            return

        for device in self.bd.paired_devices:
            if (device[0] in self.allowed_mac_addresses):
                self.allowed = True
                return

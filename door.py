import pigpio
import yaml
from time import sleep
from PigpioStepperMotor import StepperMotor, fullStepSequence
from bluedot import BlueDot
from signal import pause

def rotate():
    for i in range(nb_steps):
        motor.rotateClockwise()

    sleep(config.get('wait_time', 1))

    for i in range(nb_steps):
        motor.rotateCounterClockwise()

config = yaml.safe_load(open("config.yaml", 'r'))

pi = pigpio.pi()
motor = StepperMotor(pi, *config['pins'], sequence = fullStepSequence)
nb_steps = config.get('nb_steps', 2048)

bd = BlueDot()
bd.when_pressed = rotate

pause()
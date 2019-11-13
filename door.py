import pigpio
import yaml
from time import sleep
from PigpioStepperMotor import StepperMotor, fullStepSequence
from bluedot import BlueDot

bd = BlueDot()
bd.wait_for_press()

config = yaml.safe_load(open("config.yaml", 'r'))

pi = pigpio.pi()
motor = StepperMotor(pi, *config['pins'], sequence = fullStepSequence)

for i in range(config['nb_steps']):
    motor.rotateClockwise()

sleep(config['wait_time'])

for i in range(config['nb_steps']):
    motor.rotateCounterClockwise()

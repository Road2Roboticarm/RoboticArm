#-------------------------------------- Library Import ---------------------------------------------
import RPi.GPIO as GPIO
import time


#-------------------------------------- Global Variable --------------------------------------------
MotorDir = [
    'down',
    'up',
]

RPM_TO_STEP_DELAY = 60/(2*1600)


#------------------------------------- Class Definition --------------------------------------------
# The motor DRV8825 needs 1600 steps per turn
# To move at 60RPM, it needs 1/1600 [s] per steps
# Which means 1/3200 [s] delay between switches (2 switches per step)
# In fact it is a bit slower
class DRV8825():
    def __init__(self, dir_pin, step_pin, enable_pin):
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.enable_pin = enable_pin
        self.step = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)

    def digital_write(self, pin, value):
        GPIO.output(pin, value)

    def setPos(self, step=0):
        self.step = step

    def getPos(self):
        return self.step

    def Stop(self):
        self.digital_write(self.enable_pin, 0)

    def TurnStep(self, Dir, steps, speedRPM=60):
        # Moving Down
        if (Dir == MotorDir[0]):
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 0)
            # print('Previsous step = ', self.step)
            self.step -= steps
            # print('Steps = ', self.step)

        # Moving Up
        elif (Dir == MotorDir[1]):
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 1)
            # print('Previsous step = ', self.step)
            self.step += steps
            # print('Steps = ', self.step)

        else:
            print("the dir must be : 'down' or 'up'")
            self.digital_write(self.enable_pin, 0)
            return

        if (steps == 0):
            return

        # print("turn step:", steps)
        for i in range(steps):
            self.digital_write(self.step_pin, True)
            time.sleep(RPM_TO_STEP_DELAY/speedRPM)
            self.digital_write(self.step_pin, False)
            time.sleep(RPM_TO_STEP_DELAY/speedRPM)

    def MoveTo(self, steps, speedRPM):
        # Move up
        if steps >= self.step :
            self.TurnStep('up', (steps - self.step), speedRPM)
        
        # Move down
        else :
            self.TurnStep('down', (self.step - steps), speedRPM)

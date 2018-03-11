import piface
import RPi.GPIO as GPIO
import time

serialNumber = None
#emptyWeight = 0

# Number of times recycling bin detected garbage added to it.
num_contents = 0
# Length of sleep after detecting a falling piece of recycling
DELAY_PER_PIECE = .5



#def get_weight():

# Define Input pin
MOTION_in = 7
IR_in = 8
IR_restart = 9


def setup():
    serialNumber = hash(time.time())
    GPIO.setmode(GPIO.BCM)
    #emtpyWeight = get_weight()
    for sensor in (MOTION_in, IR_in, IR_restart):
        GPIO.setup(sensor, GPIO.IN)
    num_contents = 0


def loop():
    # Busy loop
    while True:
        if(GPIO.input(MOTION_in)):
            num_contents += 1
            time.sleep(DELAY_PER_PIECE)
            update_current_weight(num_contents, serialNumber)
        if(not GPIO.input(IR_restart)):
            start_new_collection(serialNumber)

import RPi.GPIO as GPIO


class GPIO():
    def __init__(self):
        self.button0 = 4
        self.button1 = 17
        # button2 is defined by non of the others being HIGH
        self.button3 = 27
        self.buttonPlay = 22

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.buttonPlay, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def status(self):
        if GPIO.input(self.button0):
            button = 0
            if GPIO.input(self.buttonPlay):
                play = 1
            else:
                play = 0
        elif GPIO.input(self.button1):
            button = 1
            if GPIO.input(self.buttonPlay):
                play = 1
            else:
                play = 0
        elif GPIO.input(self.button3):
            button = 3
            if GPIO.input(self.buttonPlay):
                play = 1
            else:
                play = 0
        else:
            button = 2
            if GPIO.input(self.buttonPlay):
                play = 1
            else:
                play = 0

        return (button, play)


import player
import stations
import gpio
from time import sleep

# load stations
stations = stations.load("stations.txt")

# checking gpio status and execute whatever stuff
radio = player.Player()
gpios = gpio.GPIO()
urls = []
button_old = 666
play_old = 666
while True:
    button, play = gpios.status()
    if (button != button_old) or (play != play_old):

        if (button != button_old):
            if button == 0:
                urls = [stations[0]]
            elif button == 1:
                urls = [stations[1]]
            elif button == 2:
                urls = [stations[2]]
            elif button == 3:
                urls = [stations[3]]

            if (play != play_old):
                if play:
                    if radio.getIsOn():
                        radio.transition(0)
                        radio.stop()
                    radio.start(urls)
                    sleep(1)
                    radio.transition(1)
                else:
                    radio.stop()
        if (play != play_old):
            if play:
                radio.start(urls)
                sleep(1)
                radio.transition(1)
            else:
                radio.stop()

        button_old = button
        play_old = play

    sleep(0.05)
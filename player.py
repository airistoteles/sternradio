import os
from time import sleep
from random import shuffle
import multiprocessing


class Player():
    def __init__(self):
        self.isOn = False
        self.maxVolume = 25
        self.len_init = int(os.popen("ps ax | grep -F mplayer | wc -l").read())

    def start(self, urls):
        self.stream_thread = multiprocessing.Process(target=self.shuffleMultiple, args=(urls))
        self.stream_thread.start()
        self.isOn = True
        os.system("pactl -- set-sink-volume 0 {}%".format(str(self.maxVolume)))

    def stop(self):
        # todo: volume transition when channel is switched instead stopping only
        # self.stream_thread.stop()
        self.stream_thread.terminate()
        self.isOn = False
        os.system("killall mplayer")

    def getIsOn(self):
        return self.isOn

    def setVolume(self, vol):
        self.maxVolume = vol

    def transition(self, direction):
        # direction: 1 if increasing volume
        #            0 if decreasing volume
        for i in range(self.maxVolume):
            sleep(0.001)
            if direction == 1:
                os.system("pactl -- set-sink-volume 0 +1%")
            else:
                os.system("pactl -- set-sink-volume 0 -1%")

    def stream(self, url):
        # url: string
        os.system("mplayer {} &> /dev/null &".format(url))

    def shuffleMultiple(self, urls):
        # urls: array of strings
        if len(urls) > 1:
            shuffle(urls)
        for url in urls:
            self.stream(url)
            sleep(0.5)
            while int(os.popen("ps ax | grep -F mplayer | wc -l").read()) > self.len_init:
                sleep(0.5)
            print("another")

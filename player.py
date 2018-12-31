import os
from time import sleep
from random import shuffle
import multiprocessing


class Player():
    def __init__(self):
        os.system("killall mocp")
        os.system("mocp -S")
        self.isOn = False
        self.maxVolume = 25
        self.len_init = int(os.popen("ps ax | grep -F mocp | wc -l").read())

    def start(self, urls):
        self.shuffleMultiple(urls)
        self.isOn = True
        os.system("pactl -- set-sink-volume 0 {}%".format(str(self.maxVolume)))

    def stop(self):
        # todo: volume transition when channel is switched instead stopping only
        # self.stream_thread.stop()
        #self.stream_thread.terminate()
        self.isOn = False
        os.system("mocp -P")
	#os.system("killall mocp")

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
        print("mocp -c -a -p {}".format(url))
        os.system("mocp -c -a -p {}".format(url))
#        sleep(0.5)
#        os.system("mocp -p")

    def shuffleMultiple(self, urls):
        # urls: array of strings
        if len(urls) > 1:
            shuffle(urls)
        for i in range(len(urls)):
            if i == 0:
                self.stream(urls[i])
            else:
                os.system("mocp -a {}".format(urls[i]))
            print("another")

import player
import stations
from time import sleep

# load stations
stations = stations.load("stations.txt")

# checking gpio status and execute whatever stuff
radio = player.Player()
urls = []
while True:
    print("[1] DLF \n[2] DLF Kultur \n[3] DLF Nova \n[4] DT64 \n\n[5] Stop")
    user = input("Choose station: ")
    if user == "1":
        urls = [stations[0]]
    elif user == "2":
        urls = [stations[1]]
    elif user == "3":
        urls = [stations[2]]
    elif user == "4":
        urls = [stations[3]]
    elif user == "5":
        if radio.getIsOn():
            radio.stop()
    if radio.getIsOn():
        radio.transition(0)
        radio.stop()
    radio.start(urls)
    sleep(1)
    radio.transition(1)

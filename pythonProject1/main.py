from typing import Dict
from pyowm import OWM
from pyowm.commons.databoxes import SubscriptionType
from pyowm.utils import config
from pyowm.utils import timestamps
from termcolor import colored
import os
import pygame
import time
from pyowm.utils.config import get_default_config

# code for language settings
config_dict: dict[str, str | dict[str, bool | None | int] | dict[str, str] | SubscriptionType] = get_default_config()
language = config_dict['language'] = 'fi'
# this is used for clearing the screen
clear = lambda: os.system('cls')
os.system('color')

# uses pygame to import and play background music
pygame.mixer.init()
pygame.mixer.music.load("D:\pythonProject1\M00Dy.wav")
pygame.mixer.music.play(-1,0.0)
# variable for top of menu
roof = "-"
wall = "|"
# main input for city that calls api
city = input("mikä kaupunki teitä kiinnostaa: ")
# API key and API settings
owm = OWM('b76889e1698fa0b0b5711754b0ae0a75', config_dict)
mgr = owm.weather_manager()
owm.supported_languages
#makes API call for our city variable
observation = mgr.weather_at_place(city)
w = observation.weather
#defines clouds
clouds = w.clouds
colorWall = "blue"
colorText = "red"
cityLen = len(city)
lenght1 = 20 - cityLen
wWeather = w.detailed_status
weatherLen = len(w.detailed_status)
lenght2 = 33 -weatherLen
rows = 1
wallLeng = wall.ljust(33)
#def startmenu():


#main menu of programm
def much():

    #clear()
    global rows
    print(colored(wall,colorWall)+colored(roof.ljust(65,roof),colorWall)+colored(wall, colorWall))
    print(colored(wall.ljust(33), colorWall) + colored(wall.rjust(34), colorWall))
    print(colored(wall.ljust(lenght1), colorWall) + colored(" kaupungissa ", colorText) + city.upper() + colored(" on tällä hetkellä: ","red") + colored(wall.rjust(14), colorWall))
    print(colored(wall.ljust(33), colorWall) + colored(wall.rjust(34), colorWall))
    print(colored(wall.ljust(lenght2), colorWall) +w.detailed_status+ colored(wall.rjust(34), colorWall))
    print(colored(wallLeng, colorWall) + colored(wall.rjust(34), colorWall))
    while rows <4 :
        print(colored(wallLeng, colorWall) + colored(wall.rjust(34), "blue"))
        rows = rows + 1
    print('hello')
    time.sleep(10)


def little():
    print("kaupungissa" + city + "on tällä hetkellä")
    print(w.detailed_status)


#owm = OWM('b76889e1698fa0b0b5711754b0ae0a75', config_dict)
#mgr = owm.weather_manager()
#owm.supported_languages

#observation = mgr.weather_at_place(city)
#w = observation.weather

# here you chose how much you want to see
loop=True
info = int(input("VÄHÄN TIETOA[1] PALJON TIETOA[2]: "))
while loop:

    if info == 1:
        little()
    elif info == 2:
        much()
    else:
        input("Painoit väärää nappia yritä uudelleen")

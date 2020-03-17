import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import time

dominik_geburtstag = "1.4.2001"

def xdotoolprint(text):
    breakpoint = 0
    for n,letter in enumerate(text):
        if letter == " ":
            part = text[breakpoint:n+1]
            breakpoint = n+1
            os.system("xdotool type "+ part)
            os.system("xdotool key space")
    part = text[breakpoint:]
    os.system("xdotool type "+ part)

def xdotoolprintunicode(charcode):
    os.system("xdotool key " + charcode)


def openchat(chatname):
    os.system("firefox -new-tab https://web.whatsapp.com/")
    time.sleep(10)
    os.system("xdotool key Tab")
    time.sleep(0.1)
    xdotoolprint(chatname)
    time.sleep(0.1)
    os.system("xdotool key Return")
    time.sleep(1)

def sendmessage(chatname, message):#, charcode):
    openchat(chatname)
    xdotoolprint(message)
    #xdotoolprintunicode(charcode)
    time.sleep(1)
    os.system("xdotool key Return")

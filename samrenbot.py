import irc_class as ic
from credentials import *
import os
import random
# import minitel_announcement as ma #TODO

irc=ic.IRC()
irc.connect(SERVER, PORT, CHANNEL, BOTNICK, BOTPASS) # variable from credentials file

while True:
    text = irc.get_response()

    if "PRIVMSG" in text:
        print(text.split("PRIVMSG #")[1])
    if "!hello" in text:
        irc.send(CHANNEL, "Hello!")
    if "!sing" in text:
        irc.send(CHANNEL, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

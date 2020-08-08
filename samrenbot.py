import configparser

import irc_class as ic
# import twitch_alerts.webhooks_subs as taws

# import minitel_announcement as ma #TODO

config = configparser.ConfigParser()
config.read('config.ini')
twal_cfg = config['TwitchAlert']

PORT = int(config['IRC']['PORT'])
CHANNEL = config['IRC']['CHANNEL']
BOTNICK = config['IRC']['BOTNICK']
BOTPASS = config['IRC']['BOTPASS']
CHANNEL = config['IRC']['CHANNEL']
SERVER = config['IRC']['SERVER']

irc=ic.IRC()
irc.connect(SERVER, PORT, CHANNEL, BOTNICK, BOTPASS)
follower_file = open('twitch_alerts/follow_alert.txt', 'w+')

while True:
    text = irc.get_response()
    user = text.split(":")[1].split("!")[0].capitalize()
    message = text.split(":")[-1]

    if "PRIVMSG" in text:
        print(user,":",message)
    if "!hello" in message:
        irc.send(CHANNEL, 'Hello {}!'.format(user))

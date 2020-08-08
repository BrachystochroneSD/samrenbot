import configparser

import irc_class as ic
import minylpg.minylpg as miny
from twitch_alerts.webhooks_subs import Follow_Subscription


config = configparser.ConfigParser()
config.read('config.ini')
twal_cfg = config['TwitchAlert']

PORT = int(config['IRC']['PORT'])
CHANNEL = config['IRC']['CHANNEL']
BOTNICK = config['IRC']['BOTNICK']
BOTPASS = config['IRC']['BOTPASS']
CHANNEL = config['IRC']['CHANNEL']
SERVER = config['IRC']['SERVER']

# IRC
irc = ic.IRC()
irc.connect(SERVER, PORT, CHANNEL, BOTNICK, BOTPASS)

# Subscription to twitch follow alert
follow_subs = Follow_Subscription(channel_id, client_id, lease_seconds, callback_url, oauth_token)

# Minitel
minylpg = miny.MinYLPG()

while True:
    text = irc.get_response()
    user = text.split(":")[1].split("!")[0].capitalize()
    message = text.split(":")[-1]

    with open('twitch_alerts/follow_alert.txt', 'r+') as follower_file:
        file_lines = follower_file.readlines()

        if len(file_lines) != 0:
            name = file_lines[0]
            print("New follower:", name)
            if name != "":
                minylpg.follower_alert(file_lines[0])

            # Delete firt line
            next_lines = follower_file.readlines()[1:]
            follower_file.seek(0)
            for i in next_lines:
                follower_file.write(i)
            follower_file.truncate()

    if "PRIVMSG" in text:
        print(user,":",message)
        minylpg.message(user + ":" + message)
    if "!hello" in message:
        irc.send(CHANNEL, 'Hello {}!'.format(user))

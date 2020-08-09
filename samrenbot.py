import configparser

import irc_class as ic
import twitch_alerts.webhooks_subs as twas

config = configparser.ConfigParser()
config.read('config.ini')

PORT = int(config['IRC']['PORT'])
CHANNEL = config['IRC']['CHANNEL']
BOTNICK = config['IRC']['BOTNICK']
BOTPASS = config['IRC']['BOTPASS']
CHANNEL = config['IRC']['CHANNEL']
SERVER = config['IRC']['SERVER']

client_id = config['TwitchAlert']['client_id']
oauth_token = config['TwitchAlert']['oauth_token']
channel_id = config['TwitchAlert']['channel_id']
callback_url = config['TwitchAlert']['callback_url']

# IRC
irc = ic.IRC()
irc.connect(SERVER, PORT, CHANNEL, BOTNICK, BOTPASS)

# Subscription to twitch follow alert
follow_subs = twas.Follow_Subscriptions(channel_id, client_id, callback_url, oauth_token)
follow_subs.subscribe()

while True:
    text = irc.get_response()
    user = text.split(":")[1].split("!")[0].capitalize()
    message = text.split(":")[-1]

    if "PRIVMSG" in text:
        print(user,":",message)
        with open('chat_file.txt', 'a') as chat_file: # TODO make that cleaner without text files
           chat_file.write(user + ":" + message)
    if "!hello" in message:
        irc.send(CHANNEL, 'Hello {}!'.format(user))

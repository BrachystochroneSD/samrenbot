import minylpg.minylpg as miny
from obswebsocket import obsws, requests
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

host = config['OBS']['host']
port = config['OBS']['port']
password = config['OBS']['password']

# OBS
ws = obsws(host, port, password)

# Minitel
minylpg = miny.MinYLPG()

def follow_alert(name):
    print("New follower:", name)
    ws.connect()
    current_scene = ws.call(requests.GetCurrentScene()).getName()
    if current_scene == "game scene":
        ws.call(requests.SetCurrentScene("abonnement"))
        minylpg.follower_alert(name)
        ws.call(requests.SetCurrentScene(current_scene))
    else:
        minylpg.follower_alert(name)
    ws.disconnect()

def delete_all_but_name(name):
    with open('twitch_alerts/follow_alert.txt', 'r+') as follower_file:
        lines = follower_file.readlines()
        follower_file.seek(0)
        for line in lines:
            if line != name:
                follower_file.write(line)
        follower_file.truncate()


print("Ready!")
while True:
    with open('twitch_alerts/follow_alert.txt', 'r') as follower_file:
        followers = follower_file.readlines()

    if len(followers) != 0:
        name = followers[0]
        if name != "":
            follow_alert(name)
            delete_all_but_name(name)


    with open('chat_file.txt','r+') as chat_file:
        chat_lines = chat_file.readlines()

        if len(chat_lines) != 0:
            for line in chat_lines:
                minylpg.message(line)

            # Delete all line
            chat_file.seek(0)
            chat_file.truncate()

    time.sleep(1)

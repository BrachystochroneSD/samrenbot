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

while True:
    with open('twitch_alerts/follow_alert.txt', 'r+') as follower_file:
        file_lines = follower_file.readlines()

        if len(file_lines) != 0:
            name = file_lines[0]
            print("New follower:", name)
            if name != "":
                ws.connect()
                current_scene = ws.call(requests.GetCurrentScene()).getName()
                if current_scene == "game scene":
                    ws.call(requests.SetCurrentScene("abonnement"))
                    minylpg.follower_alert(file_lines[0])
                    ws.call(requests.SetCurrentScene(current_scene))
                else:
                    minylpg.follower_alert(file_lines[0])
                ws.disconnect()

            # Delete firt line
            next_lines = follower_file.readlines()[1:]
            follower_file.seek(0)
            for i in next_lines:
                follower_file.write(i)
            follower_file.truncate()

    with open('chat_file.txt','r+') as chat_file:
        file_lines = chat_file.readlines()

        if len(file_lines) != 0:
            line = file_lines[0]
            minylpg.message(line)

            # Delete firt line
            next_lines = chat_file.readlines()[1:]
            chat_file.seek(0)
            for i in next_lines:
                chat_file.write(i)
            chat_file.truncate()

    time.sleep(1)

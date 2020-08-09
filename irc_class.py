import socket
import sys
import time

class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        self.irc.send(bytes("PRIVMSG #" + channel + " :" + msg + "\n", "UTF-8"))

    def connect(self, server, port, channel, botnick, botpass):
        # connection
        print("Connecting to: " + server)
        self.irc.connect((server, port))

        # authenfication
        print("Authenticating...")
        self.irc.send(bytes("PASS " + botpass + "\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        time.sleep(5)

        # join channel
        print("Joining channel: " + channel)
        self.irc.send(bytes("JOIN #" + channel + "\n", "UTF-8"))
        print("Joined!")

    def get_response(self):
        time.sleep(0.1)
        resp = self.irc.recv(2040).decode("UTF-8")

        if resp.find('PING') != -1:
            self.irc.send(bytes('PONG ' + resp.split()[1] + '\r\n', "UTF-8"))

        return resp

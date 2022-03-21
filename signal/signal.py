from random import randint
from json import dumps
from os import getcwd
import socket

class Signal:
    def __init__(self, socket = "/tmp/signal-cli/socket", id = randint(5000), account):
        self.signal = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.signal.connect(socket)
        self.id = id
        self.account = account

    def send_message(self, recipient, group=False, message):
        message_string = dumps({
            "jsonrpc":"2.0",
            "method":"send",
            "params":
                {
                    "account": self.account,
                    if (group):
                        "groupId": recipient,
                    else:
                        "recipient": recipient,
                    "message": message
                },
            "id": self.id
        })

        self.signal.send(message_string.encode('utf-8'))

    def send_message_attatchment(self, recipient, group=False, message, attachment):
        message_string = dumps({
            "jsonrpc":"2.0",
            "method":"send",
            "params":
                {
                    "account": self.account,
                    if (group):
                        "groupId": recipient,
                    else:
                        "recipient": recipient,
                    "message": message,
                    "attachments": [getcwd() + "/" + attachment]
                },
            "id": self.id
        })

        self.signal.send(message_string.encode('utf-8'))
from random import randint
from json import dumps
from os import getcwd
import socket

class Signal:
    def __init__(self, account, socket = "/tmp/signal-cli/socket", r_id = randint(5000)):
        self.signal = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.signal.connect(socket)
        self.id = r_id
        self.account = account

    def send_message(self, recipient, message, group=False):
        if ()
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

    def send_message_attatchment(self, recipient, message, attachment, group=False):
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
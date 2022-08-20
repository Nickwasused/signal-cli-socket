from random import randint
from json import dumps
from os import getcwd
import socket


class Signal:
    def __init__(self, account, socket_path="/tmp/signal-cli/socket", r_id=randint(0, 5000)):
        self.signal = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.signal.connect(socket_path)
        self.id = r_id
        self.account = account

    def send_message(self, recipient, message, group=False):
        if group:
            message_string = dumps({
                "jsonrpc": "2.0",
                "method": "send",
                "params":
                    {
                        "account": self.account,
                        "groupId": recipient,
                        "message": message
                    },
                "id": self.id
            })
        else:
            message_string = dumps({
                "jsonrpc": "2.0",
                "method": "send",
                "params":
                    {
                        "account": self.account,
                        "recipient": recipient,
                        "message": message
                    },
                "id": self.id
            })

        self.signal.send(message_string.encode('utf-8'))

    def send_message_attachment(self, recipient, message, attachment, group=False):
        if group:
            message_string = dumps({
                "jsonrpc": "2.0",
                "method": "send",
                "params":
                    {
                        "account": self.account,
                        "groupId": recipient,
                        "message": message,
                        "attachments": [getcwd() + "/" + attachment]
                    },
                "id": self.id
            })
        else:
            message_string = dumps({
                "jsonrpc": "2.0",
                "method": "send",
                "params":
                    {
                        "account": self.account,
                        "recipient": recipient,
                        "message": message,
                        "attachments": [getcwd() + "/" + attachment]
                    },
                "id": self.id
            })

        self.signal.send(message_string.encode('utf-8'))

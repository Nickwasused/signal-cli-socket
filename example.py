from signal-cli-socket import signal

sig = Signal("+491635558756")

# send message to a user
sig.send_message("+491625555457", True, "Hello there!")
sig.send_message_attatchment("+491625555457", "Here is the picture that you wanted.", "./photo.jpg")

# send messages to a group
sig.send_message("KBHvLSJlKKb8FQSA6Ajo5pB8/mgPjaTEbr68Mb5MwkA=", "Hello there!")
sig.send_message_attatchment("KBHvLSJlKKb8FQSA6Ajo5pB8/mgPjaTEbr68Mb5MwkA=", "Enjoy the view!", "./photo.jpg")

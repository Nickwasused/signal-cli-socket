from signal_cli_socket import Signal

sig = Signal("+491635558756")

# send message to a user
sig.send_message(["+491625555457"], "Hello there!")
sig.send_message_attachment(["+491625555457"], "Here is the picture that you wanted.", "./photo.jpg")

# send messages to a group
sig.send_message("KBHvLSJlKKb8FQSA6Ajo5pB8/mgPjaTEbr68Mb5MwkA=", "Hello there!", True)
sig.send_message_attachment("KBHvLSJlKKb8FQSA6Ajo5pB8/mgPjaTEbr68Mb5MwkA=", "Enjoy the view!", "./photo.jpg", True)

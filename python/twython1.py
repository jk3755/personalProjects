# Consumer Key (API Key)
# SBSSZ7HJrGe9UbhlKUVEPvE12
#
# Consumer Secret (API Secret)
# TI8xDTqqrKPedkJFAMbWiH2ieWBLY7eARwxqXKxgPNfHleDbAW
#
# Access Token
# 571330091-xfR91B1AIbAoDuTEcSmeKVcaqn01ZFBw2YYnXR9n
#
# Access Token Secret
# acmir7qpIZZ9B4InQEmjpM772YQ8ltRhfcW4vXGimTzNn

from twython import *
import sys



C_KEY = ("SBSSZ7HJrGe9UbhlKUVEPvE12")
C_SECRET = ("TI8xDTqqrKPedkJFAMbWiH2ieWBLY7eARwxqXKxgPNfHleDbAW")
A_TOKEN = ("571330091-xfR91B1AIbAoDuTEcSmeKVcaqn01ZFBw2YYnXR9n")
A_SECRET = ("acmir7qpIZZ9B4InQEmjpM772YQ8ltRhfcW4vXGimTzNn")

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print("Ian G. Harris is popular!")

stream= MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="Ian G. Harris")



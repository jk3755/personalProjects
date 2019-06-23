# write a python program that will access the antminer webpage, scrape values for the temperature of the three hasing boards,
# display this data in real time (updates every second) and store time interval data to monitor temperature over time (every 5 mins or so) 
# using SQL database

# import following libraries: regex, socket, time

# the antminers IP address is set for permanent DHCP at 192.168.0.107

import re
import socket
import time
import requests

from requests.auth import HTTPBasicAuth
#from requests.auth import HTTPDigestAuth

# was getting a lot of errors. entering 'chcp 65001' in the terminal fixed the issue

# r = requests.get('http://192.168.0.107:80', auth=('root', 'root'), verify=False)
# r = requests.get('http://192.168.0.107/index.html:80', auth=('root', 'root'), stream=True)
# r = requests.get(url, auth=HTTPDigestAuth('root', 'root'))
r = requests.get('http://192.168.0.107:80', auth=HTTPBasicAuth('root', 'root'))

a = r.text
#b = r.content
#c = r.json()
#d = r.raw

print(a)
#print(b)
#print(c)
#print(d)














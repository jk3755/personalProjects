
# coding: utf-8

# In[35]:

# write a python program that will access the antminer webpage, scrape values for the temperature of the three hasing boards,
# display this data in real time (updates every second) and store time interval data to monitor temperature over time (every 5 mins or so) 
# using SQL database

# import following libraries: regex, socket, time
# the antminers IP address is set for permanent DHCP at 192.168.0.107

#import socket
#import requests
#import curl
#import pycurl
#import io
#import webbrowser
#import selenium

#from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://root:root@192.168.0.107:80/")
#browser.get('http://www.yahoo.com')
#assert 'Yahoo' in browser.title

browser.quit()

print('Done')

####
#from io import StringIO
#from io import BytesIO

#username = ("root")
#password = ("root")

#buffer = BytesIO()
#c = pycurl.Curl()
#c.setopt(pycurl.USERPWD, '%s:%s' % (username, password))
#c.setopt(c.URL, 'http://192.168.0.107:80')
#c.setopt(c.WRITEDATA, buffer)
#c.perform()
#c.close()

#body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
#print(body)
####

#from requests.auth import HTTPBasicAuth
#from requests.auth import HTTPDigestAuth

# was getting a lot of errors. entering 'chcp 65001' in the terminal fixed the issue

# r = requests.get('http://192.168.0.107:80', auth=('root', 'root'), verify=False)
# r = requests.get('http://192.168.0.107/index.html:80', auth=('root', 'root'), stream=True)
# r = requests.get(url, auth=HTTPDigestAuth('root', 'root'))
#r = requests.get('http://192.168.0.107:80', auth=HTTPBasicAuth('root', 'root'))

#a = r.text
#b = r.content
#c = r.json()
#d = r.raw

#print(a)
#print(b)
#print(c)
#print(d)

###
#socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#socket1.connect( ('192.168.0.107', 80) )
#
#socket1.send(b'GET http://192.168.0.107 HTTP/1.0\n\n')
#
#while True:    
#    data = socket1.recv(512)    
#    if ( len(data) < 1 ) :        
#        break    
#        print(data)      
#socket1.close()
#
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('www.py4inf.com', 80))
#mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
#
#while True:
#    data = mysock.recv(512)
#    if(len(data) < 1):
#        break
#       print(data)
#        
#mysock.close()
###







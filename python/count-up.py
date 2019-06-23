import time

it = 0

while True:
    it = it + 1
    file = open('/home/pi/Desktop/count', 'r+')
    file.write(str(it) + ' minutes have passed.')
    time.sleep(60)
    file.close()

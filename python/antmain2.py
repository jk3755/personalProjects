import sys
import time
import datetime

import sqlite3
import paramiko

import Adafruit_CharLCD as LCD

## Initialize the LCD
lcd = LCD.Adafruit_CharLCDPlate()
## initialize ssh client
ssh = paramiko.SSHClient()
## adds auth key to list if it is unknown
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


while True:
    
    lcd.clear()
    lcd.message('Connecting...')
    
    try:
        ## connect ssh client to the host (antminer s7)
        ssh.connect('192.168.0.107', username='root', password = 'admin')
        lcd.clear()
        lcd.message('Host Connected')
        time.sleep(10)
        lcd.clear()
        ## read date from server
        stdin, stdout, stderr = ssh.exec_command("cgminer-api -o stats")
        stdin.close()
        rawdata = str(stdout.read())
        ## find temperature data and timestamp
        tempindex = (rawdata.find('temp1'))
        temp1 = int(rawdata[tempindex+6:tempindex+8])
        tempindex = (rawdata.find('temp2'))
        temp2 = int(rawdata[tempindex+6:tempindex+8])
        tempindex = (rawdata.find('temp3'))
        temp3 = int(rawdata[tempindex+6:tempindex+8])
        timestamp = (datetime.datetime.now())
        pass
    except:
        continue

    ## create database if does not exist. otherwise commit current data
    try:
        db = 'tempdata.sqlite'
        open('tempdata.sqlite')
        # Connecting to the database file
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("INSERT INTO tempdata VALUES ('{stamp}', {temp1}, {temp2}, {temp3})"\
                  .format(stamp=timestamp, temp1=temp1, temp2=temp2, temp3=temp3))
        ## Committing changes and closing the connection to the database file
        conn.commit()
        conn.close()

        ## Update the LCD display
        lcd.clear()
        display = ("Core Temperature\n1:" + str(temp1) + " 2:" + str(temp2) + " 3:" + str(temp3))
        lcd.message(display)
        time.sleep(10)
        
    except: 
        db = 'tempdata.sqlite'
        table = 'tempdata'
        coltime = 'timestamp'
        coltemp1 = 'core 1 temp'
        coltemp2 = 'core 2 temp'
        coltemp3 = 'core 3 temp'
        column_type_int = 'INTEGER'  
        field_type_str = 'STRING'
    
        # Connecting to the database file
        conn = sqlite3.connect(db)
        c = conn.cursor()
    
        c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
            .format(tn=table, nf=coltime, ft=field_type_str))

        # Add other columns
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                .format(tn=table, cn=coltemp1, ct=column_type_int))

        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                .format(tn=table, cn=coltemp2, ct=column_type_int))

        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                .format(tn=table, cn=coltemp3, ct=column_type_int))

        c.execute("INSERT INTO tempdata VALUES ('{stamp}', {temp1}, {temp2}, {temp3})"\
                .format(stamp=timestamp, temp1=temp1, temp2=temp2, temp3=temp3))

        ## Committing changes and closing the connection to the database file
        conn.commit()
        conn.close()
    

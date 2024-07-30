#### GUI ALWAYS RUNNING ON LAN -- Local Live CSI Monitoring using data from remote Nexmon Device
## Sent to this device using BT connection
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak import BleakScanner, BleakClient
from http.server import BaseHTTPRequestHandler, HTTPServer


#### WHEN A FIRE IS DETECTED, THIS FILE WILL BE CALLED ON RASPBERRY PI ZERO W

## 1. Enable Light on Attached RPI (Flashing Red)


## 2. Push Warning to GUI


## 3. If Internet enabled, send an email to an address
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("The tempurature has been detected at XXXXXXXXX")

msg['Subject'] = "Warning! A Potential Fire has been detected using CSI!!!"
msg['From'] = "csiwarner@000800.xyz"
msg['To'] = "z5488711@ad.unsw.edu.au"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

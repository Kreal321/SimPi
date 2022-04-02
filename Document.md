## JSON between client and server format
```
{
    data: int/string/array
    type: int
}
```
### Type 0: server message
Display on screen

### Type 1: client message
Start/Suspend/Resume/Stop actions of SimPi

### Type 2: simpi config queue
Queue of actions 

### Type 3: Multi-client management
The number of current connected clients

### Type 4: debug message from server
Display on console

### Type 5: simpi status
Simpi status

### Type 6: simpi config file names
server to client

### Type 7: simpi config file data
server to client

### Type 8: simpi config file option
client to server

## SimPi Queue Options
```
{
    type: int
    options: int/string/array
}
```
#### 1. Start
Start `type: 10` \
Click to start `type: 11`

~#### 2. Suspend~
~Suspend `type: 20` \~
~Click to suspend `type: 21`~

~#### 3. Resume ~
~Resume `type: 30` \~
~Click to resume `type: 31`~

#### 4. Stop
Stop `type: 40` \
~Click to stop `type: 41`~

#### 5. Wait
Wait X mins `type: 50` \
Wait until X `type: 5X`

#### 6. Source
Open Source `type: 61` \
Close Source `type: 62`

#### 7. Audio
Play Audio `type: 71`

#### 8. If Statement
If X `type: 8X` \
End if `type: 80`

#### 9. loop several times

## Raspberry Pi GPIO
- Pin 3 = 110B
- Pin 2 = 110A
- Pin 4 = 110C
- Pin 17 =110D
- Pin 27 = 5VA
- Pin 22 = 5VB
- Pin 10 = 12VA
- Pin 9 = switch
- Pin 11 = Falling Input

### Testing
```
try
low1
high1
```

## Raspberry pi
User name: Pi
Password: raspberry

## Documents
 - Bootstrap v5.1.3 [Documation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
 - websockets Documations: [Python](https://websockets.readthedocs.io/en/stable/index.html), [Javascript](https://javascript.info/websocket)
 - Raspberry Pi GPIO: [Python]( https://sourceforge.net/p/raspberry-gpio-python/wiki/browse_pages/)

## TP-Link
Model No. TL-WR802N \
Set as client mode.
```
Default:
SSID: TP-Link_7610
Wifi Password: 85313415

Now:
SSID: TP-Link_7610
Wifi Password: simpibox

Manage Page
Page: tplinkwifi.net
Password: simpibox2022
```

## Raspberry Pi start up
Edit start up
```
sudo crontab -e
```

Add command line
```
@reboot sudo /home/pi/Desktop/simpi.py > log.txt &
```
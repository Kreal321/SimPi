# SimPi
An interface used in Simpi box based on Raspberry Pi that can supplement simulator functions or enhance simulation environment

## Table of Content
- [File structure](#file-structure)
- [Server Requirements](#server-requirements)
- [Set up server environment on Raspberry Pi](#set-up-server-environment-on-raspberry-pi)
- [Start server locally](#start-server-locally)
- [Start server remotely](#start-server-remotely)
  * [Server is on Linux](#server-is-on-linux)
  * [Server is on Windows](#server-is-on-windows)
- [Start Client](#start-client)
- [Server side error fixing](#server-side-error-fixing)
- [Reinstall server from Github](#reinstall-server-from-github)
- [Change log](#change-log)

## File structure
```
.
├── Client                        # Client files
│   ├── asset                     # Assets files for web application
│   │   ├── css                   # Css files for client side
│   │   ├── fonts                 # Icon fonts files for client side 
│   │   ├── icon                  # Icon demo files
│   │   └── js                    # JavaScripts files for client side
│   └── index.html                # Main page of the web application
├── Server                        # Server files
│   ├── __pycahe__                # Bytecode cache python files
│   ├── Config                    # Config folder storing cfgs as JSON files
│   ├── Install                   # Files for installing
│   ├── audio.py                  # Audio class handling audio subprocess (play/pause/resume/stop)
│   ├── config.py                 # Config class handling save/update/delete/read cfg files
│   ├── main.py                   # Entry point of the sever
│   ├── messager.py               # Messger class handling send and receive messages between client and server
│   ├── messages.py               # Messages class decode message from client and encode message to client
│   ├── simpi.py                  # Simpi class handling simpi background subprocess
│   ├── simpiController.py        # Simpi background controller
│   └── simpiProcessController.py # Simpi background process controller
├── Test                          # Auto test folder
├── docs                          # Github page root path
├── Document.md                   # Doc for developing
├── README.md                     # Readme file for setting up server on raspberry pi
├── remote.bat                    # Batch file for starting server on local network (windows)
└── remote.sh                     # Batch file for starting server on local network (linux)
```

## Server Requirements
 - python >= 3.5
 - websockets  Documations: [Python](https://websockets.readthedocs.io/en/stable/index.html), [Javascript](https://javascript.info/websocket)
 - multiprocessing support: psutil module
 - audio support: playsound module
 - allow python to connect to public network in firewall if you want to run it remotely




## Set up server environment on Raspberry Pi
Update `apt`
```
sudo apt-get update -y
```
Install `websockets`
```
sudo apt-get install -y python3-websockets
```
Install `psutil`
```
sudo apt-get install -y python3-psutil
```
Install `Raspberry Pi GPIO`
```
sudo apt-get install -y rpi.gpio
```
Install `playsound`
```
sudo pip3 install playsound==1.2.2 
sudo apt install python3-gst-1.0
```
Check `python` version
```
python3 --version
```

If python version < 3.5, install `python 3.7`. \
Required python version >= 3.5
```
sudo apt install python3.7
```

## Start server locally
Run server.py
```
python3 server.py
```

## Start server remotely
### Server is on Linux
Run remote.sh on Linux
```
sudo chmod +x remote.sh
./remote.sh
```

### Server is on Windows
Run remote.bat on windows
```
start remote.bat
```

## Start Client
1. Run index.html \
Or open https://kreal321.github.io/SimPi/ in browser

2. Connect to server
```
Connect to the ip address show in the server terminal
e.g. Connect to 127.0.0.1 if server is run locally
```

3. Set up SimPi Queue from options or Read config files


## Server side error fixing
1. Manully kill process
```
sudo killall sudo python3
```
2. Run Server maunally
```
cd Desktop/SimPi
./remote.sh
```

## Reinstall server from Github
1. Delete previous folder
```
cd Desktop
rm -rf SimPi
```
2. Pull from Github
```
cd Desktop
./git.sh
```

## Change log
## 4/21/2022
- update installation guide, develop doc and user manual

## 4/19/2022
- Audio bugs fix
- Add play/pasue/resume/stop audio options
- Docs updates

## 4/13/2022
- fix GPIO bugs
- Perform system tests

## 4/12/2022
- If statement
- Add show debug button
- Add background

## 4/7/2022
- UI design

## 4/2/2022
- File save and load features

## 3/28/2022
- Add auto start button

### 3/24/2022
- Drag and drop features
- ICON design
- Impletement delete
- Make Simpi option sticky to the top
- Fix button bugs

### 3/22/2022
- Fix Stop simpi option bug
- Add Simpi Queue UI
- Fix setinterval endless loop error

### 3/21/2022
- Fix child process cannot send message bug
- Add simpi status check

### 3/20/2022
- Update GPIO ports
- Add test cases

### 3/10/2022
- Add server to start up
- Connection redesign
- Add auto connection
- Messages redesign
- Add debug messages

### 3/8/2022
- Fix putty connection time out

### 3/4/2022
- Test audio on simpi box

### 3/3/2022
- Fix GPIO Ports bugs
- Add GPIO Ports support on server

### 3/1/2022
- Test audio
- Add audio option for simpi option
- Add aduio for server
- Import mpg123
- Add server audio class
- Add server audio support

### 2/25/2022
- Test hardware connection

### 2/24/2022
- Import Raspberry Pi GPIO
- Set up testing for GPIO

### 2/18/2022
- Executable Start button
- Simpi server side queue redesign
- Executable Waituntil button

### 2/13/2022
- Update doc
- Simpi Queue UI Design

### 2/12/2022
- Fix suspend and resume bugs
- Server now can decode simpi queue
- Server can print Simpi Queue on screen
- Add button display to queue on client side

### 2/11/2022
- Add loop X times
- Add open/close source
- Add signals in server
- Client now can send messages to child process

### 2/8/2022
- Change SimPi queue options

### 2/7/2022
- Add Option class in server
- Add shared signals array
- Redesign SimPi queue

### 2/3/2022
- Add SimPi queue Send button
- Redesign SimPi queue options

### 2/2/2022
- Client-side Simpi queue draft
- Client-side click to start, suspend, click to resume, resume, wait x minutes
- Create github page for simpi

### 1/30/2022
- Add Multi-client detection and warning

### 1/28/2022
- Add JSON for message communcitating
- Add encoding and decoding functions for server and client slides

### 1/27/2022
- Add Bootstrap to client
- Beautify the interface
- Add start/suspend/resume/stop buttons
- Add Server screen

### 1/26/2022
- Made some changes on simpi and simpiController
- Change files path, add server, path, build folders
- Fix linux suspend bugs

### 1/25/2022
- Seperate server.py file
- Create Messager class for send and receive messages
- Create messages for encoding and decoding JSON later
- Fix suspend/resume simpi none type bugs
- Add stop method

### 1/24/2022
- Add documation for server.py file
- Add start action for Simpi process
- Add status checking when start/suspend/resume a Simpi process

### 1/23/2022
- Add multiprocessing to handle background simpi process
- Create SimpiProcessController class to better control background child process
- Add suspend and resume method for SimpiProcessController
- Create Simpi class to handle actions

### 1/22/2022
- Add remote connection
- Add windows batch file to start server just one click
- Add unix shell script to start server just one click

### 1/20/2022
- Initialize Repository
- Bidirectional communication between javascript and python Test
# SimPi
An interface used in Simpi box based on Raspberry Pi that can supplement simulator functions or enhance simulation environment

## Table of Content
- [File structure](#file-structure)
- [Server Requirements](#server-requirements)
- [Set up server environment](#set-up-server-environment)
- [Start server locally](#start-server-locally)
- [Start server remotely](#start-server-remotely)
  * [Server is on Linux](#server-is-on-linux)
  * [Server is on Windows](#server-is-on-windows)
- [Start Client](#start-client)
- [Change log](#change-log)

## File structure
```
.
├── Client                        # Client files
│   ├── asset                     # Assets files for web application
│   └── index.html                # Main page of the web application
├── Server                        # Server files
│   ├── __pycahe__                # Bytecode cache python files
│   ├── Install                   # Files for installing
│   ├── main.py
│   ├── messager.py 
│   ├── messages.py
│   ├── simpi.py
│   ├── simpiController.py
│   └── simpiProcessController.py
├── docs                          # Github page root path
├── Document.md                   # Doc for developing
├── README.md                     # Readme file
├── remote.bat                    # Batch file for starting server on local network (windows)
└── remote.sh                     # Batch file for starting server on local network (linux)
```

## Server Requirements
 - python >= 3.5
 - websockets  Documations: [Python](https://websockets.readthedocs.io/en/stable/index.html), [Javascript](https://javascript.info/websocket)
 - psutil  
 - allow python to connect to public network in firewall if you want to run it remotely


## Set up server environment
Update apt
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

Check python version
```
python3 --version
```

If python version < 3.5, install `python 3.7`. Required python version >= 3.5
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
Run index.html \
Or Go to https://kreal321.github.io/SimPi/

Run index.html \
Connect to the ip address show in the server terminal \
e.g. Connect to `127.0.0.1` if server is run locally



## Change log
### 2/7/2022
- Add Option class in server

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
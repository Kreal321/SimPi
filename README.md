# SimPi

## Table of Content
- [Requirement](#requirement)
- [Set up on raspberry](#set-up-on-raspberry)
- [Set up on raspberry with command line](#set-up-on-raspberry-with-command-line)
- [Start server locally](#start-server-locally)
- [Start server remotely](#start-server-remotely)
  * [Server is on Linux](#server-is-on-linux)
  * [Server is on Windows](#server-is-on-windows)
- [Change log](#change-log)

## Requirement
 - python >= 3.5
 - websockets  Documations: [Python](https://websockets.readthedocs.io/en/stable/index.html), [Javascript](https://javascript.info/websocket)
 - psutil  
 - allow python to connect to public network in firewall if you want to run it remotely



## Set up on raspberry
Install the latest version of Paspberry Pi OS

Update apt
```
sudo apt-get update -y
```
Install websockets
```
sudo apt-get install -y python3-websockets
```
Install psutil
```
sudo apt-get install -y python3-psutil
```

Check python version
```
python3 --version
```
Require python >= 3.5


Install python 3.7
```
sudo apt install python3.7
```

## Set up on raspberry with command line
Install git
```
sudo apt install git
git clone https://github.com/Kreal321/SimPi.git
```

Update apt
```
sudo apt-get update -y
```
Install websockets
```
sudo apt-get install -y python3-websockets
```
Install psutil
```
sudo apt-get install -y python3-psutil
```


## Start server locally
Run server.py
```
python3 server.py
```

Run index.html \
Connect to 127.0.0.1

## Start server remotely
### Server is on Linux
Run remote.sh on Linux
```
sudo chmod +x remote.sh
./remote.sh
```

Run index.html \
Connect to the ip address show in the server terminal

### Server is on Windows
Run remote.bat on windows for testing
```
start remote.bat
```

Run index.html \
Connect to the ip address show in the server terminal




## Change log
### 1/25/2022
- Sepearte server.py file
- Create Clients class for send and receive messages
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
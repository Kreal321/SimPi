# SimPi

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
sudo apt-get install -y psutil
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
### 1/23/2022
- Add multiprocessing to handle background simpi process
- Create SimpiProcess class to better control background child process
- Add suspend and resume method for SimpiProcess
- Create Simpi class to handle actions

### 1/22/2022
- Add remote connection
- Add windows batch file to start server just one click
- Add unix shell script to start server just one click

### 1/20/2022
- Initialize Repository
- Bidirectional communication between javascript and python Test
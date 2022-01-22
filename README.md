# SimPi

## Requirement
 - python >= 3.5
 - websockets [Python](https://websockets.readthedocs.io/en/stable/index.html), [Javascript](https://javascript.info/websocket)
 - allow python to connect to public network in firewall if you want to run it remotely



## Set up
Update apt
```
sudo apt-get update -y
```

Install python 3.7
```
sudo apt install python3.7
```
Install websockets
```
sudo apt-get install -y python3-websockets
```

## Start server locally
Run server.py
```
python3 server.py
```

Run index.html \
Connect to 127.0.0.1

## Start server remotely
Run remote.bat
```
start remote.bat
```

Run index.html \
Connect to the ip address show in the server terminal



## Change log
### 1/22/2022
- Add remote connection

### 1/20/2022
- Initialize Repository
- Bidirectional communication between javascript and python Test
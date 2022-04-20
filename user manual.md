# User Manual

## Table of Content
- [Set up server environment on Raspberry Pi](#set-up-server-environment-on-raspberry-pi)
- [Start server locally](#start-server-locally)
- [Start server remotely](#start-server-remotely)
  * [Server is on Linux](#server-is-on-linux)
  * [Server is on Windows](#server-is-on-windows)
- [Start Client](#start-client)
- [Server side error fixing](#server-side-error-fixing)
- [Reinstall server from Github](#reinstall-server-from-github)

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

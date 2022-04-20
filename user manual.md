# User Manual

## Table of Content
- [System Overview](#system-overview)
- [System Summary](#system-summary)
- [System Requirements](#system-requirements)
- [Set up server environment on Raspberry Pi](#set-up-server-environment-on-raspberry-pi)
- [Start server locally](#start-server-locally)
- [Start server remotely](#start-server-remotely)
  * [Server is on Linux](#server-is-on-linux)
  * [Server is on Windows](#server-is-on-windows)
- [Start Client](#start-client)
- [Troubleshooting](#Troubleshooting)
  * [Server side error fixing](#server-side-error-fixing)
  * [Reinstall server from Github](#reinstall-server-from-github)

## System Overview
Often during simulation, elements within the simulated environment need to be supplemented and controlled. Many off-the-shelf devices that allow for this have limited control, limited power sources, and lack portability. Also, these devices can lack an easy programming language or ease-of-use interface and can be costly.

SimPi provides a platform that can control different power sources, provide relay switching, and multimedia output with an interface running on a browser, which allows users to create routines by dragging and dropping actions (AC outlet on/off) and conditions to move forward, hold, or loop. SimPi aims to provide a platform that can provide controlled power to multiple devices requiring either AC or DC voltage. In addition to power, this device provides the ability to build small custom circuits right on the device, open and close circuits (switches), and output multimedia content via HDMI. The market of small devices and pre-assembled circuits is vast due to the popularity of the Raspberry Pi computer and like products within the hobby and teaching communities. The use of these types of devices can lead to many innovative applications within the medical simulator and simulation environment. 

## System Summary
The SimPi device and interface that can provide both AC and DC voltage along with switching to different devices to control peripheral components in the simulation environment which can be used to train clinical students.

## System Requirements
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
Or open https://kreal321.github.io/SimPi/ in browser \
And you will get a page like this:

![](images/openpage.jpg?raw=true "Title")

2. Connect to server
```
Connect to the ip address show in the server terminal
e.g. Connect to 127.0.0.1 if server is run locally
```
Click `Auto Connect`, and then the client will try to connect to the server and shows `Connecting`

![](images/serverconnection.jpg?raw=true "Title")

![](images/serverconnecting.jpg?raw=true "Title")

 When you see a green `Connected`, means you have connected to the server

 ![](images/serverconnected.jpg?raw=true "Title")

  When you see a red `Failed to connect`, means the connection failed, so you need to check the server and wifi setting. See more at [Troubleshooting](#troubleshooting)

 ![](images/serverfail.jpg?raw=true "Title")

3. Set up SimPi Queue from options 

You can create your customed SimPi Queue from `Options`

 ![](images/options.jpg?raw=true "Title")

 ![](images/simpiqueue.jpg?raw=true "Title")

You can also move or delete a option that is not in the correct place
 
 ![](images/deleteoption.jpg?raw=true "Title")

4. Upload SimPi Queue to the server

After you set up your queue, you just need to click `Upload queue to server`

 ![](images/uploadq.jpg?raw=true "Title")

**Remember to set `Start` and `Stop` in each queue**

 ![](images/startstop.jpg?raw=true "Title")

5. Save and Load cfg files from server

You can also save your customed queue to the server:

 ![](images/cfgfile.jpg?raw=true "Title")


# Troubleshooting

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

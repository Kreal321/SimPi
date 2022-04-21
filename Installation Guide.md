# Installation Guide
## Install SimPi server on a new Raspberry Pi 2
1. [System Requirements](#system-requirements) 
2. [Install Raspberry Pi OS using Raspberry Pi Imager](#install-raspberry-pi-os-using-raspberry-pi-imager)
3. [Set up server environment on Raspberry Pi OS](#set-up-server-environment-on-raspberry-pi-os)
4. [Download SimPi server from Github](#download-simpi-server-from-github)
5. [Set SimPi auto Start up](#set-simpi-auto-start-up)

## System Requirements
 - Hardware: Raspberry Pi 2 with a router or Raspberry Pi 4
 - Software: Latest Raspberry Pi OS

## Install Raspberry Pi OS using Raspberry Pi Imager
1. Download Raspberry Pi Imager: [Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe), [macOS](https://downloads.raspberrypi.org/imager/imager_latest.dmg), [Ubuntu](https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb)
2. Open Raspberry Pi Imager

![](images/raspberrypiimager.jpg?raw=true "Title")

3. Choose Operating System. You need to choose **Raspberry Pi OS (32-bit)** if you are using Raspberry Pi 2

![](images/chooseos.jpg?raw=true "Title")

4. Choose a storage
5. Writing and wait for success

## Set up server environment on Raspberry Pi OS
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
Install `playsound` and its dependence `gst`
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

## Download SimPi server from Github
1. cd to Desktop
```
cd Desktop
```
2. clone SimPi respository from Github
```
git clone https://github.com/Kreal321/SimPi.git
```

## Set SimPi auto Start up
Edit start up
```
sudo crontab -e
```

Add command line
```
@reboot sudo /home/pi/Desktop/simpi.py > /home/pi/Desktop/log.txt &
```

## After this, you are all set
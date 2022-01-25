#!/bin/bash
local_ip=$(ifconfig | grep '\<inet\>'| grep -v '127.0.0.1' | awk '{print $2}' | awk 'NR==1')

sudo python3 server/main.py remote $local_ip
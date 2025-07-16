#!/bin/bash
read -p "USB Server IP: " IP
read -p "Bus ID (e.g., 1-1): " BUSID

usbip attach -r "$IP" -b "$BUSID"

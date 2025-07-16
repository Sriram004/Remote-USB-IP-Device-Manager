#!/bin/bash
usbip port
read -p "Enter port number to detach: " PORT
usbip detach -p "$PORT"

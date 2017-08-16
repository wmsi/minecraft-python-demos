#!/bin/bash -e
# A simple script to install these scripts and codes in convenient locations 
# on a Mac with MinecraftEdu installed.

# codes
cp -fr ../codes/* ~/Documents/Minecraft\ Pi\ Codes/
cp ./reset-mac.sh ~/Desktop/
cp ./copyFlat-mac.sh ~/Desktop/
cp -fr ../flatWorld-mac ~/Documents/

# transfer files
bash ./reset-mac.sh
bash ./copyFlat-mac.sh

# Make shortcut
ln -s ~/Library/Application\ Support/minecraftedu/minecraft/mcpimods/python/ ~/Desktop/Minecraft\ Python\ Codes

echo Installed!

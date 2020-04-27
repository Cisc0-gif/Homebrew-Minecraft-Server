@echo off 
title Minecraft Server Console 
echo ======================================== 
echo  
echo Starting Homebrew Minecraft Server... 
echo /op [YOU] to give yourself admin perms
echo 
echo ======================================== 
java -Xmx1024M -Xms1024M -jar server.jar nogui 

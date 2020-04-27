#! /usr/bin/env python3

import os
import requests
import socket
from colorama import Fore, Back, Style

java = input("Is Java installed?[y/N]: ")
if java == 'n' or java == 'N':
  os.system('sudo apt-get install default-jre')
else:
  print(Fore.CYAN + '========================================')
  print('\n[*]Starting Homebrew Minecraft Server...\n')
  print('[*]Enter ^C or ^Z To Stop Server...\n')
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80)) 
  r = requests.get("http://ifconfig.me").text
  print('[*]Private Server IP: ' + str(s.getsockname()[0]) + ':25565\n')
  print('[*]Public Server IP: ' + str(r) + ':25565\n')
  print('[*]Use /op *you* to make yourself admin\n')
  print('========================================' + Style.RESET_ALL)
  os.system('sudo java -Xmx1024M -Xms1024M -jar server.jar nogui')

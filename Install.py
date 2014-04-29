#Install the dependencies for MinecraftOven
import os #Import modules
print('If errors were thrown, try running this program as root or run "sudo Install.py"')
print('Copying the API from ~/mcpi/api/python/mcpi/ to ~/mcpi/_mods/mcpi/')
os.system('cp -r ./api/python/mcpi/ ./_mods/') #Copy the API
print('The API requires pygame to run.')
print('Installing pygame...')
os.system('apt-get install python-pygame') #Install dependencies
print('Install complete')
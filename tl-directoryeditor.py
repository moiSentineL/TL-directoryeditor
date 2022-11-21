import os
import sys
import time
from colorama import init, Fore
from pyjavaproperties import Properties

propertiesfiledir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'JavaPortableLauncher','Data', 'AppData', '.tlauncher', 'tlauncher-2.0.properties'))
minecraftdir = os.path.realpath(os.path.join(os.path.dirname(__file__),'..', 'JavaPortableLauncher','Data', 'AppData', '.minecraft'))
rawmcdir = repr(minecraftdir).replace("'", "")

init(convert=True)

print(Fore.YELLOW + "TLauncher Directory Editor")
print("----moiSentineL----")

time.sleep(1)

def countdown():
    count = 3
    while count > 0:
        print(Fore.YELLOW + "Exiting in",str(count) + "...", end="\r")
        time.sleep(1)
        count = count - 1

def propertieseditor():
    p = Properties()
    p.load(open(propertiesfiledir))
    p['minecraft.gamedir'] = f'{rawmcdir}'
    p.store(open(propertiesfiledir, 'w'))
    # print (p['minecraft.gamedir'])
def existence():      
    try:
        if os.path.exists(propertiesfiledir):
            print("\nProperies file found.")
            time.sleep(0.5)
            print("Checking if .minecraft folder exists or not...")
            time.sleep(1)
            
            try:
                if os.path.exists(minecraftdir):
                    print("\n.minecraft folder found.")
                    time.sleep(0.5)
                    print("Commiting Changes.")
                    propertieseditor()
                    
                    time.sleep(2)
                    
                    print("\nDirectory changed")
                    print("Edited directory: ", rawmcdir)
                    countdown()
                else:
                    print("\n.minecraft folder not found.")
                    time.sleep(0.5)
                    print("Creating folder...")
                    os.mkdir(minecraftdir)

                    time.sleep(2)

                    print("\nFolder created")
                    print("Edited directory: ", rawmcdir)
                    countdown()
            except:
                print(Fore.RED + "Something's Wrong")
                countdown()
        else:
            print(Fore.RED + "Something's Wrong")
            countdown()
    except:
        print(Fore.RED + "Something's Wrong")
        countdown()

print('\nChecking if tlauncher-2.0.properties file exists or not...')
existence()

    

import os
import sys
import time
from colorama import init, Fore
from pyjavaproperties import Properties

propertiesfiledir = r"JavaPortableLauncher\Data\AppData\.tlauncher\tlauncher-2.0.properties"
minecraftdir = os.path.realpath(os.path.join(os.path.dirname(__file__), 'JavaPortableLauncher','Data', 'AppData', '.minecraft'))
rawmcdir = repr(minecraftdir).replace("'", "")

init(convert=True)

print(Fore.YELLOW + "TLauncher Directory Editor")
print("----moiSentineL----")

time.sleep(1)

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
                else:
                    print(Fore.RED +"Something's Wrong")
                    os.system('pause')
            except:
                print(Fore.RED + "Something's Wrong")
                os.system('pause')
        else:
            print(Fore.RED + "Something's Wrong")
            os.system('pause')
    except:
        print(Fore.RED + "Something's Wrong")
        os.system('pause')

print('\nChecking if tlauncher-2.0.properties file exists or not...')

existence()

    

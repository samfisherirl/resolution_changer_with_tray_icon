import pystray
import pywintypes
import win32api
import win32con
from PIL import Image
from pystray import MenuItem as item

from os import getcwd
import os.path

localdir = getcwd()
menu = []

def on_set_resolution(width: int, height: int):
    # adapted from Peter Wood: https://stackoverflow.com/a/54262365
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth: int = width
    devmode.PelsHeight: int = height

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode, 0)


def iterate_resolutions_from_file():
    # The code starts by opening the file "resolutions.txt" and reading in all of its lines into a list called resolutions.
    # The code then iterates over each line, splitting it on commas to get two integers, x and y.
    # The next part of the code creates a menu item with an action that sets the resolution for x=x and y=y to whatever is passed as a parameter (in this case 'on_set_resolution(int(x), int(y))').
    # The code sets the resolution of the screen to a specific value.     
    
    with open((os.path.join(localdir, 'resolutions.txt')), 'r') as f:
        for resolutions in f.readlines():
            
            resolutions = resolutions.split(',') 
            
            x = int(resolutions[0].strip())
            y = int(resolutions[1].strip())
            
            val = f"Swith to: {x}x{y} resolution"
            
            menu.append(item(val, lambda:  on_set_resolution(int(x), int(y))),)
            
    return menu
    




def on_quit():
    icon.visible = False
    icon.stop()


if __name__ == "__main__":
    # adapted from Sebastin Ignacio Camilla Trinc: https://stackoverflow.com/a/48284187
    
    image = Image.open((os.path.join(localdir, "icon.ico")))
    
    menu = iterate_resolutions_from_file()
    menu.append(item('Quit', on_quit))
    menu = tuple(menu)
    
    icon = pystray.Icon("Resolution Switcher", image, "Resolution Switcher", menu)
    icon.run()

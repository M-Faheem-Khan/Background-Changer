# Simple background changer WINDOWS only
# HOW IT WORKS
# removing bg_image.jpeg from desktop
# Download random 1920x1080 image
# Set as desktop background

# imports
import os
import ctypes
import requests
from datetime import datetime

# setting the file name
name = os.getcwd() + "\\bg_image.jpeg"
# removing bg_image from desktop on each start
try:
	os.remove(name)
except:
	pass
	
# downloading the image from the picsum api
r = requests.get("https://picsum.photos/1920/1080/?random", allow_redirects=True)
open(name, "wb").write(r.content)

# printing time and letting the user know the image has been downloaded download 
print(str(datetime.now().time)[:8])
print("%s has been downloaded" % (name))

# setting the background image
print("Setting the background image")
ctypes.windll.user32.SystemParametersInfoA(20, 0, name , 0)

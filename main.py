from PIL import Image
import os
import numpy as np

strBright = "¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;^:,'.`  "

img = Image.open("image.jpg")
img.convert('RGB')
rows, columns = os.get_terminal_size() 
height, widht = img.size
brMap = []
strFinal = ""


for x in range(columns):
    for y in range(rows):
        yPos, xPos = x*(height//columns), y*(widht//rows)
        pixelRBG = img.getpixel((xPos, yPos))
        R,G,B = pixelRBG
        brightness = round(sum([R,G,B])/12)
        brMap.append(brightness)

for i in range(len(brMap)): 
    strFinal += strBright[(brMap[i]-1)-1]

print(strFinal)

import cv2 
import numpy as np
import mss
import pyautogui 
import matplotlib.pyplot as plt
import time

pyautogui.PAUSE = 0.00001

def prepareImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,0, 1,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return thresh
    
def findObject(image):
    if 0 in image:
        return True
    
    return False

x = 470
y = 330
width = 140
height = 1

cactus_monitor = {"top": y, "left": x, "width": width, "height": height}

yb = 297
b_width = 50
bird_monitor = {"top": yb, "left": x, "width": b_width, "height": height}


with mss.mss() as sct:
    while True:
        jump = False
        # bird = False
        image = np.array(sct.grab(monitor=cactus_monitor))
        # image_bird = np.array(sct.grab(monitor=bird_monitor))
        
        cactus = prepareImage(image) 
        # image_bird = prepareImage(image_bird)
        
        part1 = cactus[0][:45]
        part2 = cactus[0][100:]
        
        # if findObject(image_bird):
        #     pyautogui.press('down')
        #     bird = True
        if findObject(part1):
                pyautogui.press('up')
                jump = True
                
        if findObject(part2) and jump:
                pyautogui.press('down')
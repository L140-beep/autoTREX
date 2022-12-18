import cv2 
import numpy as np
import mss
import pyautogui 
import matplotlib.pyplot as plt
import time


def prepareImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,0, 1,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return thresh
    
def findObject(image):
    if 0 in image:
        return True
    
    return False

x = 470
y = 300
width = 30
height = 38

monitor = {"top": y, "left": x, "width": width, "height": height}

x_diff = 130
width_diff = 100
monitor1 = {"top": y, "left": x + x_diff, "width": width + width_diff, "height": height}

start_time = time.time()

ctime = 0

with mss.mss() as sct:
    while True:
        jump = False
        image = np.array(sct.grab(monitor=monitor))
        image1 = np.array(sct.grab(monitor=monitor1))
        
        cactus = prepareImage(image) 
        image1 = prepareImage(image1)
        
        
        if findObject(cactus):
                pyautogui.press('up')
                jump = True
                
        if findObject(image1) and jump:
                pyautogui.press('down')
                
        current_time = int(time.time() - start_time)
        
        if ctime != current_time:
            
            if current_time % 10 == 0:
                x += (current_time // 10) * 2
                x_diff += 5
                width_diff += 10
                monitor = {"top": y, "left": x, "width": width, "height": height}
                monitor1 = {"top": y, "left": x + x_diff, "width": width + width_diff, "height": height}
            ctime = current_time
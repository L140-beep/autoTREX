import cv2 
import numpy as np
import mss
import pyautogui 
import matplotlib.pyplot as plt
import time

pyautogui.PAUSE = 0.0001

def findCactus(image):
    if 0 in image:
        return True
    
    return False

x = 470
y = 317
width = 100
height = 1

monitor = {"top": y, "left": x, "width": width, "height": height}




with mss.mss() as sct:
    while True:
        jump = False
        image = np.array(sct.grab(monitor=monitor))
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray,0, 1,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        part1 = thresh[0][:40]
        part2 = thresh[0][99:]
        
        if findCactus(part1):
            pyautogui.press('up')
            jump = True
        if findCactus(part2) and jump:
            pyautogui.press('down')
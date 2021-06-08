import pyautogui
import time
import random
import AppKit
info = AppKit.NSBundle.mainBundle().infoDictionary()
info["LSBackgroundOnly"] = "1"

pyautogui.FAILSAFE = False
while True :
    time.sleep(180)
    for i in range(40,150):
        pyautogui.moveTo(random.randint(500,550), i*5)
    for i in range(0,3):
        pyautogui.press('shift')

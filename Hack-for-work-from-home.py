import pyautogui
import time
pyautogui.FAILSAFE=False   #just to ensure the module will work
while True:   #To keep the computer on
    time.sleep(10) 
    for i in range(0,100):  #how many times will the cursor move 


        pyautogui.moveTo(5,i*5)     ## it will move   (500 pixels) 0,5,10,15...500(pixles) on y axis                  #To move the cursor(we have to initialize the X and Y direction)
            # time.sleep(10)   #first waits for 10 sec
        
    for i in range(0,3):
        pyautogui.press('shift')

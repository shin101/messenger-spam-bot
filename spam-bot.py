import pyautogui
import time 

while True:
    time.sleep(4)
    pyautogui.typewrite("insert your message here")
    time.sleep(2)
  
    pyautogui.press('enter')
    break

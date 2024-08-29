import pyautogui
import time

pyautogui.moveTo(1860, 22, 1)

pyautogui.doubleClick()

time.sleep(5)

pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter'])
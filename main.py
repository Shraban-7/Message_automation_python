import pyautogui
import time

x = int(input())
while x:
    time.sleep(4)
    pyautogui.typewrite("Hello")
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.typewrite("How are you?")
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.typewrite("If you want to ask any question please ask me")
    time.sleep(4)
    pyautogui.press("enter")
    x = x - 1

import pyautogui
import time


print("Press Ctrl-C to quit.")
try:
    while True:
        length, width = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()

        if currentMouseX >= 0 and currentMouseX < length:
            pyautogui.moveTo(currentMouseX + 1, None)
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX - 1, None)
        else:
            pyautogui.moveTo(currentMouseX - 1, None)
        time.sleep(2)


except KeyboardInterrupt:
    print("\n")

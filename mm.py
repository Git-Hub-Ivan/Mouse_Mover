import pyautogui
import time


print("Press Ctrl-C to quit. 3 Times")
try:
    while True:
        length, width = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()

        if currentMouseX >= 0 and currentMouseX < length:
            pyautogui.moveTo(currentMouseX + 1, None)
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX - 1, None)
            localtime = time.localtime()
            result = time.strftime("%I:%M:S %p", localtime)
            currentMouseX, currentMouseY = pyautogui.position()
            print('Moved at ' + str(result) + '. FromTo (' +str(currentMouseX) + ', ' +str(currentMouseY)+')')
        else:
            pyautogui.moveTo(currentMouseX - 1, None)
        time.sleep(90)


except KeyboardInterrupt:
    print("\n")

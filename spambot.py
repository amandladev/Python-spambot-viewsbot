import pyautogui, time

time.sleep(5)
f = open("spamtext",'r')
for word in f:

    pyautogui.typewrite(word)
    pyautogui.press("enter")
import pyautogui as pg
import time

time.sleep(5)

ups = 1
n = 1

while ups <= 200:

    pg.typewrite(str(n))
    n = n + 1
    pg.typewrite(["tab"])
    ups = ups + 1


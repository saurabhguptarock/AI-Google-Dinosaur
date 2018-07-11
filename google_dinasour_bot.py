from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinate:
    replayBtn = (480, 293)
    dinasaur = (178, 300)


def restartGame():
    pyautogui.click(Cordinate.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')


def imagegrab():
    box = (214, Cordinate.dinasaur[1] - 10, 255, Cordinate.dinasaur[1] + 30)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restartGame()
    while True:
        if imagegrab() != 1887:
            pressSpace()
            time.sleep(0.1)


main()

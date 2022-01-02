# designed by CJ Moshy on 12/15/2021

import pyautogui as pg
import time
import keyboard as k


# simple Python autoclicker script, designed for AFK farming a mob grinder in minecraft
# to use this properly, have a weapon in your '1' slot, and food in your '2' slot

def eat():
    k.press('2')
    pg.mouseDown(button="right")
    time.sleep(5)
    k.press('1')


def clicker():
    time.sleep(5)
    k.press('1')
    x = 0
    while True:
        x += 1
        if x == 500:
            eat()
            x = 0
        pg.click()
        time.sleep(1.5)
        if k.is_pressed('x'):
            break


def main():
    clicker()


if __name__ == "__main__":
    main()

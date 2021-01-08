# -*- coding: utf-8 -*-
from pyautogui import *
import pyautogui
import time
import keyboard
import random

RANDOM_INTERVAL = random.randint(1,4)

def click(x_loc,y_loc):
    pyautogui.click(clicks=2, interval=0.25, x=x_loc, y=y_loc)

def buy(type, image_filename, position):
    if position != None:
        print("Buy" + type)

        item_button = pyautogui.center(position)
        click(item_button[0] + 800, item_button[1] + 50)
        time.sleep(1) # wait for confirm button

        buy_button_location = pyautogui.locateOnScreen(image_filename, confidence=0.95)
        print(image_filename)
        print(buy_button_location)

        buy_button=pyautogui.center(buy_button_location)
        pyautogui.moveTo(buy_button[0], buy_button[1])

        click(buy_button[0], buy_button[1])
        time.sleep(RANDOM_INTERVAL)
    else:
        print("No " + type + " to buy.")

def scroll_to_bottom(refresh_button):
    print("scrolling")
    mid_screen = refresh_button[0] + refresh_button_width
    drag_amount = mid_screen / 4 * -1 # negative to drag down

    pyautogui.moveTo(mid_screen, refresh_button[1])
    pyautogui.drag(0, drag_amount, 1, button='left')

    time.sleep(RANDOM_INTERVAL)

def refresh_shop(refresh_button):
    print("refreshing")
    click(refresh_button[0], refresh_button[1])
    time.sleep(0.5) # wait for confirm to appear

    confirm_button_pos = pyautogui.locateOnScreen('confirm button.png', confidence=0.95)
    confirm_button=pyautogui.center(confirm_button_pos)
    click(confirm_button[0], confirm_button[1])
    time.sleep(RANDOM_INTERVAL) # wait for new list to load

while keyboard.is_pressed('q') == False:
    refresh_button_pos = pyautogui.locateOnScreen('refresh_button.PNG', confidence=0.95)
    refresh_button = pyautogui.center(refresh_button_pos)
    refresh_button_width = refresh_button_pos[2]

    covenant_pos = pyautogui.locateOnScreen('covenant.png', confidence=0.95)
    mystic_pos = pyautogui.locateOnScreen('mystic.png', confidence=0.95)
    time.sleep(0.5)

    # check if bookmarks in initial list
    buy("covenant", "Buy_button_Covenant.png", covenant_pos)
    buy("mystic", "Buy_button_Mystic.png", mystic_pos)

    # scroll down to check final item
    scroll_to_bottom(refresh_button)

    # check if final item is a bookmark
    covenant_pos = pyautogui.locateOnScreen('covenant.png', confidence=0.95)
    mystic_pos = pyautogui.locateOnScreen('mystic.png', confidence=0.95)
    buy("covenant", "Buy_button_Covenant.png", covenant_pos)
    buy("mystic", "Buy_button_Mystic.png", mystic_pos)

    refresh_shop(refresh_button)
    

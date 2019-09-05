#!/usr/bin/python3

import time
import threading
import ctypes

WORK_DURATION = 600
LONG_BREAK_EVERY = 4
BREAK_EVERY = 4

TITLE = 'pybreak'
MAIN_MENU_TEXT = 'Press OK to end session.'
SHORT_BREAK_TEXT = 'Go take a short break! Press OK when finished.'
LONG_BREAK_TEXT = 'Go take a long break! Press OK when finished.'

MAIN_MENU_ICON = 0x00000
BREAK_ICON = 0x40000

MessageBox = ctypes.windll.user32.MessageBoxW

def main():
    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    menu_popup()

def loop():
    while True:
        time.sleep(WORK_DURATION)
        if i % LONG_BREAK_EVERY == 0:
            break_popup(LONG_BREAK_TEXT)
        else:
            break_popup(SHORT_BREAK_TEXT)

def menu_popup():
    MessageBox(None, MAIN_MENU_TEXT, TITLE, MAIN_MENU_ICON)

def break_popup(text):
    MessageBox(None, text, TITLE, BREAK_ICON)
            
if __name__=='__main__':
    main()

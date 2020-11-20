'''automate an app or programme with pyautogui - basic commands'''

'''
pyautogui uses pictures and according to the image it finds that 'button'
on the app, take screenshots of the 'buttons' you want to press (etc) and
indicate each time / use the command time.sleep() after each command to the
pyautogui if the proccessor is too slow

pyautogui uses the mouse and the keyboard exactly like you would do,
you can't use them at the same time
keep away from the computer until the code ends running
'''

import os
import pyautogui
import time

#open app
path = '...'
os.startfile(path)
#wait 10 secs for it to open
time.sleep(10)

#path of the pngs that we will use
pngs_path = "..."
files_path = "..."

#click on something specific
pyautogui.click(pyautogui.locateCenterOnScreen(pngs_path+'image_of_the_button.png'))

#write something
pyautogui.write('cd '+files_path)

#press enter
pyautogui.press('enter')

#move the cersor on something without clicking it
pyautogui.moveTo(pyautogui.locateCenterOnScreen(pngs_path+'image.png'))

#press right click
pyautogui.rightClick()

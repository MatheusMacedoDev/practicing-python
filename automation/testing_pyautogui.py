import pyautogui as pa
import time

pa.PAUSE = 0.2

pa.press('win')
pa.write('firefox')
pa.press('enter')
pa.write('youtube.com')
pa.press('enter')

time.sleep(3)

pa.click(620, 144)
pa.write('neovim')
pa.press('enter')

time.sleep(5)

pa.click(751, 321)

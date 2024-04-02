import pyautogui as pa
import time
import clipboard

pa.PAUSE = 0.2

pa.press('win')
pa.write('terminal')
pa.press('enter')

time.sleep(1)

pa.getActiveWindow()

clipboard.copy('cd /mnt/d/Files/Projects/paysys-backend/')
pa.hotkey('ctrl', 'v')

pa.press('enter')

clipboard.copy('nvim ./')
pa.hotkey('ctrl', 'v')

pa.press('enter')
pa.press('enter')

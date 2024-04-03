import pyautogui as pa
import time
import clipboard

pa.PAUSE = 0.2

time.sleep(1)

pa.press('win')
pa.write('docker')
pa.press('enter')

time.sleep(2)

pa.press('win')
pa.write('terminal')
pa.press('enter')

time.sleep(1)

w = pa.getActiveWindow()
w.activate()

clipboard.copy('cd /mnt/d/Files/Projects/paysys-backend/')
pa.hotkey('ctrl', 'v')

pa.press('enter')

clipboard.copy('nvim ./')
pa.hotkey('ctrl', 'v')

pa.press('enter')
pa.press('enter')

pa.hotkey('ctrl', 'shift', '5')

time.sleep(1)

clipboard.copy('cd /mnt/d/Files/Projects/paysys-backend/')
pa.hotkey('ctrl', 'v')
pa.press('enter')

time.sleep(1)

pa.write('tmux new -s Backend')
pa.press('enter')

pa.hotkey('ctrl', 'b')
time.sleep(.5)
pa.press('d')

pa.write('tmux new -s Commands')
pa.press('enter')

time.sleep(2)

clipboard.copy('docker start ab4f2da4ba1d')
pa.hotkey('ctrl', 'v')
pa.press('enter')

clipboard.copy('docker start 6d50a892ce74')
pa.hotkey('ctrl', 'v')
pa.press('enter')

pa.hotkey('alt', 'tab')
pa.hotkey('alt', 'F4')


#left half & zoom 75%

import pyautogui as pag
import time
import keyboard
from playsound import playsound
print(pag.position())
#prev_x = 200; prev_y = 1000
#next_x = 700; next_y = 1000
prev_x = 434; prev_y = 1356
next_x = 1251; next_y = 1354


def run():
    while True:
        while True:
            if keyboard.is_pressed("q"): return
            pag.click(next_x, next_y, duration=0.1)
            if keyboard.is_pressed("q"): return
            time.sleep(0.2)
            if keyboard.is_pressed("q"): return
            #res_icon = pag.locateOnScreen('./reservation.PNG', region=(400,100,500,700))
            #res_icon = pag.locateOnScreen('./reservation2.png', region=(1290,9400,1410,980))
            #res_icon = pag.locateOnScreen('./reservation2.PNG', region=(1286,313, 300, 700))
            #res_icon = pag.locateOnScreen('./reservation2.png', region=(400,100,700,900))
            print(f'Searching availiable reservation...')
            res_icon = pag.locateOnScreen('./reservation2.png', confidence=0.8)
            print(f'Done')
            if keyboard.is_pressed("q"): return
            print(f'Search reservation icon result:{res_icon}')
            if res_icon is not None:
                print(f'found reservation icon!')
                break
            else:
                pag.click(prev_x, prev_y, duration=0.1)
        print(f'found reservation icon:{res_icon}')
        pag.click(res_icon, duration=0.1)
        pag.click(next_x, next_y, duration=0.1)
        time.sleep(0.1)

        #plus_icon = pag.locateOnScreen('./plus.PNG', region=(400,200,700,600))
        plus_icon = pag.locateOnScreen('./plus.PNG', confidence=0.8)
        print(f'plus icon:{plus_icon}')
        pag.click(plus_icon, duration=0.1)
        pag.click(next_x, next_y, duration=0.1)
        time.sleep(0.1)

        ng = pag.locateOnScreen('./ng.PNG', region=(100,100,1000,800))
        print(f'ng message:{ng}')

        if ng is not None:
            pag.click(ng.left+40, ng.top+105, duration=0.1)
            pag.click(prev_x, prev_y, duration=0.1)
        else :
            break
    return

if __name__ == '__main__':
    run()
    playsound('sound.mp3')
#pag.click(185, 934, duration=0.1)
#pag.click(618, 934, duration=0.1)
#pag.click(185, 934, duration=0.1)
#pag.click(618, 934, duration=0.1)
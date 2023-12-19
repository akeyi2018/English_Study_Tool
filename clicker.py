import mouse as ms
import time
from pynput import keyboard, mouse

ctl = 0

def click_tiktok():
    ms.move(250, 600)
    for i in range(1,500):
        if ctl == 0:
            ms.double_click()
            time.sleep(0.5)
        else:
            break

def scroll_tiktok():
    ms.move(250, 600)
    for i in range(1,100):
        if ctl == 0:
            ms.wheel(-3)
            time.sleep(10)
        else:
            break

def release(key):
    print('{0} が離されました'.format(key))
    global ctl
    # ctl = 1
    if key == keyboard.Key.esc:     # escが押された場合
        # listener.stop()   # listenerを止める
        ctl = 1
        

def press(key):
    try:
        print('アルファベット {0} が押されました'.format(key.char))
    except AttributeError:
        print('スペシャルキー {0} が押されました'.format(key))

sg = int(input())

time.sleep(3)
listener = keyboard.Listener(
    on_press=press,
    on_release=release)
listener.start()

# sg = int(input())
if sg == 1:
    click_tiktok()
else:
    scroll_tiktok()

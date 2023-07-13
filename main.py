import pyautogui
from time import sleep

position = pyautogui.position()
pixel_color = pyautogui.pixel(position.x, position.y)





def wait():
    sleep(0.1)
    
def Cactus_finder():
    position = pyautogui.position()
    pixel_color = pyautogui.pixel(position.x, position.y)
    
    print(pixel_color)

    if pixel_color == (172, 172, 172):
        pyautogui.press("space")
        
while True:
    try:
        Cactus_finder()
    except KeyboardInterrupt:
        exit()


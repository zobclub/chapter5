from microbit import *
import random

a = [1,2,3,4,5]

def showLedbar():
    for i in range(5):
        for x in range(5):
            if x < a[i]:
                display.set_pixel(x,i,9)
            else:
                display.set_pixel(x,i,0)

while True:
    if button_a.is_pressed():
        for i in range(4):
            r = random.randint(0, 4-i)
            a[i], a[r] = a[r], a[i]
        showLedbar()
    elif button_b.is_pressed():
        for i in range(4):
            for j in range(4-i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        showLedbar()
    sleep(200)
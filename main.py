import time
import pyautogui as pg


def delete_friend():
    pg.move(450, -30)
    time.sleep(0.3)
    pg.move(0, 100, 0.3)
    pg.click()


number_of_friends = int(input("Enter number of friends: "))
fr_h = number_of_friends * 105  # length of friends list in pixels
scr_h = pg.size()[1] - 165  # length of visible friends screen
scrollheight = scr_h - 210
rolls = int(fr_h // scrollheight)

for z in range(2, 0, -1):  # time to get ready
    print(f"Start in {z}")
    time.sleep(1)
print('START')

counter = 0
try:
    for roll in range(rolls):
        # print('scroll', roll)
        dogs = pg.locateAllOnScreen('dog.png')
        for dog in dogs:
            if dog[1] < pg.size()[1] - 110:
                pg.moveTo(dog, duration=0.2)
                delete_friend()
                counter += 1
                print('Del:', counter)
                pg.moveTo(dog, duration=0.2)
        pg.vscroll(-scrollheight)
        if dogs:
            time.sleep(0.3)
except KeyboardInterrupt:
    print('Stopped by user')
print(f"Unfriended {counter} DELETED friends" if counter else "No DELETED friends found")

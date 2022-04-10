from random import randint
apple = Actor("apple")
#kiwi = Actor("kiwi")
orange = Actor("orange")
pineapple = Actor("pineapple")
def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()

place_apple()

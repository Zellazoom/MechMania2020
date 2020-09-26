import random
inv = []


# lists go "Right", "Forward", "Left", "Backward"
room1 = ['a wall', 'a locked door', 'a bobby pin on a drawer', "a boarded up window"]
room2 = ['a mirror', 'a boarded up window', 'a shelf with a flashlight', 'a hallway']
entryway1 = ['another locked door', 'a hallway', 'a hallway', 'a room']
hallfoward1 = ['some kind of picture', 'a boarded up window', 'a living room', 'the entryway']
hallleft1 = ['a kitchen', 'a boarded up window', 'a room', 'a hallway']
startroom1 = ['a wall', 'the entry way', 'a drawer', "a boarded up window"]
livingroom1 = ['a tv', 'a dining room', 'a couch', 'a hallway']
diningroom1 = ['a picture of an island', 'a table with chairs', 'a kitchen', 'a living room']
kitchen1 = ['a drawer', 'a hallway', 'some appliances', 'a dining room']


def inventory():
    global inv
    print(inv)


def instructions():
    print("This is a text based adventure game in early stages. There might be some bugs.")
    print('The point of the game is escape?!')
    print("")
    print("Basic Commands:")
    print(" look 'Left','Right','forward','back' = looking commands")
    print("'Go there' = go to the place your looking at")
    print(" Grab 'object' = grab an object")
    print("Open 'object' = open an open-able object")
    print("use Yes and No to answer a question")
    print("Press ENTER to move on.")
    move_on = input("").lower()
    if move_on == "enter".lower():
        game()
    else:
        pass


def game():
    print("")
    print('*You wake up in a dark room.*')
    print("*You are all alone with a door in front of you.*")
    print("*You have nothing in you inventory...*")
    print("Press ENTER to move on.")
    move_on = input("").lower()
    if move_on == "enter".lower():
        game()
    else:
        pass


def endgame():
    print("The End... To be continued?")
    reset = input("Would you like to play again?")
    if reset == 'Yes'.lower():
        start_game()
    if reset == 'No'.lower():
        print('Well... Live long and prosper.~Spock~')


def open_door():
    print("Sweet! I can get out of here.")
    print("*You open the door and walk out of the room.*")
    inv.remove('Bobby pin')
    print(inv)
    look2()


# print (*inv)
def look1():  # room that starts out
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("How to get open this door...").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", room1[0], "there.")
            movearea += 0
        if direction == 'Look Forward'.title():
            print("There is", room1[1], "there.")
            if input() == 'open door'.lower():
                if 'Bobby pin' not in inv:
                    print("*The door is locked.*")
                if 'Bobby pin' in inv:
                    movearea += 1
                    open_door()
            else:
                pass
        if direction == 'Look Left'.title():
            print("There is", room1[2], "there.")
            if input() == 'Grab bobby pin'.lower():
                inv.append('Bobby pin')
                print(inv)
        if direction == 'Look Back'.title():
            print("There is", room1[3], "there.")
        else:
            pass


def emptyroom1():  # room after unlocked door
    print("I must be in a room.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("Why would I go back in here...").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", startroom1[0], "there.")
            movearea += 0
        if direction == 'Look Forward'.title():
            print("There is", startroom1[1], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                look2()
        if direction == 'Look Left'.title():
            print("There is", startroom1[2], "there.")
            if input() == 'open drawer'.lower():
                print("*You open the drawer.*")
                print("There is a jacket, shirt, and pants in here.")
                if input() == 'Grab jacket'.lower():
                    inv.append('jacket')
                    print(inv)
                if input() == 'Grab shirt'.lower():
                    inv.append('shirt')
                    print(inv)
                if input() == 'Grab pants'.lower():
                    inv.append('pants')
                    print(inv)
                else:
                    emptyroom1()
            else:
                emptyroom1()

        if direction == 'Look Back'.title():
            print("There is", startroom1[3], "there.")
            movearea += 0
        else:
            pass


def look2():  # number 2/ the entryway
    print("I must be in an entryway.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("Where to go...").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", entryway1[0], "there.")
            if input() == 'open door'.lower():
                if 'key' not in inv:
                    print("*The door is locked.*")
                    shout = input("Should I yell for help?").lower()
                    if shout == 'Yes'.lower():
                        print("*You yell out the door.")
                        print("*Then you hear footsteps come to the door as you scream even more.")
                        print("*The door opens...")
                        print("*BANG!*")
                        print("*YOU DIED...")
                        movearea += 1
                        endgame()
                    if shout == 'No'.lower():
                        movearea += 0
                        print("I wonder if someones trying to keep me here.")
                    else:
                        movearea += 0
                if 'key' in inv:
                    movearea += 1
                    print("You have escaped... For Now")
                    endgame()
            else:
                pass
        if direction == 'Look Forward'.title():
            print("There is", entryway1[1], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                forward1()
        if direction == 'Look Left'.title():
            print("There is", entryway1[2], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                left1()

        if direction == 'Look Back'.title():
            print("There is", entryway1[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                emptyroom1()

        else:
            pass


# hallway forward from entryway
def forward1():
    print("I am in a hallway.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("Ok now what...").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", hallfoward1[0], "there.")
            movearea += 0
        if direction == 'Look Forward'.title():
            print("There is", hallfoward1[1], "there.")
            movearea += 0
        if direction == 'Look Left'.title():
            print("There is", hallfoward1[2], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                livingroom()
        if direction == 'Look Back'.title():
            print("There is", hallfoward1[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                look2()
        else:
            pass


# left hallway from entry way
def left1():
    print("I am in a hallway.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("What to do...").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", hallleft1[0], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                kitchen()
        if direction == 'Look Forward'.title():
            print("There is", hallleft1[1], "there.")
            movearea += 0
        if direction == 'Look Left'.title():
            print("There is", hallleft1[2], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                room2a()
        if direction == 'Look Backward'.title():
            print("There is", hallleft1[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                look2()
        else:
            pass


def room2a():  # second room
    print("I am in a room.")
    movearea = 0
    global inv
    while movearea != 1:
        direction = input("What's in here?").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", room2[0], "there.")
            movearea += 0
        if direction == 'Look Forward'.title():
            print("There is", room2[1], "there.")
            movearea += 0
        if direction == 'Look Left'.title():
            print("There is", room2[2], "there.")
            if input() == 'Grab flashlight'.lower():
                inv.append('flashlight')
                print("Yes I got a flashlight. Now I can see in darker places.")
                inventory()
        if direction == 'Look Back'.title():
            print("There is", room2[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                left1()
        else:
            pass


def livingroom():
    print("I am in a living room.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", livingroom1[0], "there.")
            movearea += 0
        if direction == 'Look Forward'.title():
            print("There is", livingroom1[1], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                diningroom()
        if direction == 'Look Left'.title():
            print("There is", livingroom1[2], "there.")
            movearea += 0
        if direction == 'Look Back'.title():
            print("There is", livingroom1[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                forward1()
        else:
            pass


def diningroom():
    print("I am in a dining room.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", diningroom1[0], "there.")
            movearea += 0
        if direction == 'Look Forward'.title():
            print("There is", diningroom1[1], "there.")
            movearea += 0
        if direction == 'Look Left'.title():
            print("There is", diningroom1[2], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                kitchen()
            else:
                pass

        if direction == 'Look Back'.title():
            print("There is", diningroom1[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                livingroom()
    else:
        pass


def kitchen():
    print("I am in a kitchen.")
    global inv
    movearea = 0
    while movearea != 1:
        direction = input("").title()
        mouse_loc()
        if direction == 'Look Right'.title():
            print("There is", kitchen1[0], "there.")
            if input() == 'open drawer'.lower():
                print("*You open the drawer.*")
                if 'flashlight' in inv:
                    print("There is a screwdriver, key, and a couple pens in here.")
                    if input() == 'Grab key'.lower():
                        inv.append('key')
                        print(inv)
                    if input() == 'Grab screwdriver'.lower():
                        inv.append('screwdriver')
                        print(inv)
                    if input() == 'Grab pens'.lower():
                        inv.append('pens')
                        print(inv)
                    if input() == 'back'.lower():
                        kitchen()
                else:
                    print("It's so dark I can't see anything.")
            else:
                kitchen()
        if direction == 'Look Forward'.title():
            print("There is", kitchen1[1], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                left1()
        if direction == 'Look Left'.title():
            print("There is", kitchen1[2], "there.")
            movearea += 0
        if direction == 'Look Back'.title():
            print("There is", kitchen1[3], "there.")
            if input() == 'Go there'.lower():
                movearea += 1
                diningroom()
    else:
        pass


def mouse_game():
    print("What was that...")
    should_i = input("").lower()
    if should_i == 'inspect'.lower():
        print("*You look around and see a mouse scurrying across the floor.*")
        print("Oh... that's a mouse")
    if should_i == 'stay'.lower():
        print("*You wait and stay quiet for a minute*")
        print("I hope there is nothing here with me...")
    else:
        pass


def mouse_loc():
    random_mouse = random.randint(0, 8)
    if random_mouse == 1:
        mouse_game()


# Start of Game
def start_game():
    print("       __________________________________________________________________________________________________ ")
    print("      /      \   /  _____            __         /\  /\   [ ]   /|  /| [ ] _____     ___                 / ")
    print("     /        \ /   |   |   |   |   |          /  \/  \   |    \   \   |  |   |   |-   \               /  ")
    print("    /__________/____|___|___|___|___|_________/________\__|___|/__|/___|__|___|___|____|______________/   ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("          _______     _____       _____        ___       _______    _______     __                        ")
    print("          |  ____|   /  ___\     / ___ \      / _ \      |  ___ \   |  ____|   |  |                       ")
    print("          |  |___    | |___     / /   \/     / /_\ \     |  |__| |  |  |___    |  |                       ")
    print("          |  ____|    \___ \   |  |         /  ___  \    |  ____/   |  ____|   |__|                       ")
    print("          |  |___     ____| |   \ \___/\   / /     \ \   |  |       |  |___     __                        ")
    print("          |______|    \____/     \_____/  /__|     |__\  |__|       |______|   |__|                       ")
    username = input('Hello what is your name?')
    print("Hello", username)
    commence_game = input("Would you like to play a game? Yes or No").title()
    if commence_game == 'No'.title():
        print("okay then. Your lost not mine...")
    elif commence_game == 'Yes'.title():
        instructions()
        game()
        look1()


start_game()

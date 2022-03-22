import sys,time,random,os
from telnetlib import X3PAD
from art import *

instructionboard = """
        |        |  
    1   |    2   |    3
________|________|________
        |        |
    4   |    5   |    6
________|________|________
        |        |
    7   |    8   |    9
        |        |
"""
os.system('cls')

def randomnum():
    random.choice("123456789")


def tw(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)

def startgame():
    print("PLAYER = X")
    print("AI = X")
    playerx1 = [" ", " ", " "]
    playerx2 = [" ", " ", " "]
    playerx3 = [" ", " ", " "]
    aix1 = [" ", " ", " "]
    aix2 = [" ", " ", " "]
    aix3 = [" ", " ", " "]
    tie = ["X", "X", "X"]
    winifp1 = ["X", "X", "X", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", "X", " ", " ", " ", " ", "X"]
    winifp2 = [" ", " ", " ", "X", "X", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X", " ", " ", "X", " "]
    winifp3 = [" ", " ", " ", " ", " ", " ", "X", "X", "X", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", "X", "X", " ", " "]

    winifa1 = ["O", "O", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", "O", " ", " ", " ", "O", "O", " ", " ", " ", " ", "O"]
    winifa2 = [" ", " ", " ", "O", "O", "O", " ", " ", " ", "O", " ", " ", " ", "O", " ", " ", " ", "O", " ", "O", " ", " ", "O", " "]
    winifa3 = [" ", " ", " ", " ", " ", " ", "O", "O", "O", "O", " ", " ", " ", "O", " ", " ", " ", "O", " ", " ", "O", "O", " ", " "]
    randomn = "123456789"
    def checkwinplayer():
        ind1 = 0
        ind2 = 3
        for i in range(8):
            if playerx1 == winifp1[ind1:ind2] and playerx2 == winifp2[ind1:ind2] and playerx3 == winifp3[ind1:ind2]:
                print(f"""
        |        |  
    {x1}   |    {x2}   |    {x3}   
________|________|________
        |        |
    {x4}   |    {x5}   |    {x6}   
________|________|________
        |        |
    {x7}   |    {x8}   |    {x9}   
        |        | 
        """)
                print("PLAYER WINS THE GAME!")
                time.sleep(5)
                mainmenu()
            elif aix1 == winifa1[ind1:ind2] and aix2 == winifa2[ind1:ind2] and aix3 == winifa3[ind1:ind2]:
                print(f"""
        |        |  
    {x1}   |    {x2}   |    {x3}   
________|________|________
        |        |
    {x4}   |    {x5}   |    {x6}   
________|________|________
        |        |
    {x7}   |    {x8}   |    {x9}   
        |        | 
        """)
                print("AI WINS THE GAME!")
                time.sleep(5)
                mainmenu()
            elif x1 == x2 == x3 == x4 == x5 == x6 == x7 == x8 == x9:
                print("TIE BATTLE!")
                time.sleep(5)
                mainmenu()
            else:
                ind1 = ind1 + 3
                ind2 = ind2 + 3
        

    os.system('cls')
    print(text2art("3"))
    time.sleep(0.5)
    os.system('cls')
    print(text2art("2"))
    time.sleep(0.5)
    os.system('cls')
    print(text2art("1"))
    time.sleep(0.5)
    os.system('cls')
    aix = 0
    playerx = False
    x1=x2=x3=x4=x5=x6=x7=x8=x9 = " "
    print(instructionboard)
    turn = True
    while True:
        if playerx == True:
            checkwinplayer()
        else:
            pass
        if turn == True:
            print(f"""
        |        |  
    {x1}   |    {x2}   |    {x3}   
________|________|________
        |        |
    {x4}   |    {x5}   |    {x6}   
________|________|________
        |        |
    {x7}   |    {x8}   |    {x9}   
        |        | 
        """)
            userinput = input("Player:")
            print(f"You Choose {userinput}")
            playerx = True
            if userinput == "1":
                print("")
                if x1 == " ":
                    x1 = "X"
                    playerx1[0] = "X"
                    randomn.replace("1", "")
                    turn = False
                    continue
                else:
                    print("1 is already filled")
                    pass
            elif userinput == "2":
                print("")
                if x2 == " ":
                    x2 = "X"
                    playerx1[1] = "X"
                    randomn.replace("2", "")
                    turn = False
                    continue
                else:
                    print("2 is already filled")
                    pass
            elif userinput == "3":
                print("")
                if x3 == " ":
                    x3 = "X"
                    playerx1[2] = "X"
                    randomn.replace("3", "")
                    turn = False
                    continue
                else:
                    print("3 is already filled")
                    pass
            elif userinput == "4":
                print("")
                if x4 == " ":
                    x4 = "X"
                    playerx2[0] = "X"
                    randomn.replace("4", "")
                    turn = False
                    continue
                else:
                    print("4 is already filled")
                    pass
            elif userinput == "5":
                print("")
                if x5 == " ":
                    x5 = "X"
                    playerx2[1] = "X"
                    randomn.replace("5", "")
                    turn = False
                    continue
                else:
                    print("5 is already filled")
                    pass
            elif userinput == "6":
                print("")
                if x6 == " ":
                    x6 = "X"
                    playerx2[2] = "X"
                    randomn.replace("6", "")
                    turn = False
                    continue
                else:
                    print("6 is already filled")
                    pass
            elif userinput == "7":
                print("")
                if x7 == " ":
                    x7 = "X"
                    playerx3[0] = "X"
                    randomn.replace("7", "")
                    turn = False
                    continue
                else:
                    print("7 is already filled")
                    pass
            elif userinput == "8":
                print("")
                if x8 == " ":
                    x8 = "X"
                    playerx3[1] = "X"
                    randomn.replace("8", "")
                    turn = False
                    continue
                else:
                    print("8 is already filled")
                    pass
            elif userinput == "9":
                print("")
                if x9 == " ":
                    x9 = "X"
                    randomn.replace("9", "")
                    playerx3[2] = "X"
                    turn = False
                    continue
                else:
                    print("9 is already filled")
                    pass
            elif userinput == "/menu":
                mainmenu()
            else:
                print("Wrong Input")
                turn = True
                continue
        else:
            ainum = random.choice(randomn)
            if ainum == "1":
                print("")
                if x1 == " ":
                    print(f"AI Choose {ainum}")
                    x1 = "O"
                    aix1[0] = "O"
                    randomn.replace("1", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "2":
                print("")
                if x2 == " ":
                    print(f"AI Choose {ainum}")
                    x2 = "O"
                    aix1[1] = "O"
                    randomn.replace("2", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "3":
                print("")
                if x3 == " ":
                    print(f"AI Choose {ainum}")
                    x3 = "O"
                    aix1[2] = "O"
                    randomn.replace("3", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "4":
                print("")
                if x4 == " ":
                    print(f"AI Choose {ainum}")
                    x4 = "O"
                    aix2[0] = "O"
                    randomn.replace("4", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "5":
                print("")
                if x5 == " ":
                    print(f"AI Choose {ainum}")
                    x5 = "O"
                    aix2[1] = "O"
                    randomn.replace("5", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "6":
                print("")
                if x6 == " ":
                    print(f"AI Choose {ainum}")
                    x6 = "O"
                    aix2[2] = "O"
                    randomn.replace("6", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "7":
                print("")
                if x7 == " ":
                    print(f"AI Choose {ainum}")
                    x7 = "O"
                    aix3[0] = "O"
                    randomn.replace("7", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "8":
                print("")
                if x8 == " ":
                    print(f"AI Choose {ainum}")
                    x8 = "O"
                    aix3[1] = "O"
                    randomn.replace("8", "")
                    turn = True
                    continue
                else:
                    pass
            elif ainum == "9":
                print("")
                if x9 == " ":
                    print(f"AI Choose {ainum}")
                    x9 = "O"
                    aix3[2] = "O"
                    randomn.replace("9", "")
                    turn = True
                    continue
                else:
                    pass


def settings():
    os.system('cls')
    settingstitle = text2art("Settings")
    print(settingstitle)
    print("\n")
    print("[1]  | Credits")
    print("[2]  | Back to menu")
    print("Settings on development")
    while True:
        print("\n")
        settingsinput = input("Menu Select: ")
        if settingsinput == "2":
            os.system('cls')
            mainmenu()
        elif settingsinput == "1":
            tw("""
            ------------
            Tools Used:
            ------------
            Visual Studio Code - Code Editor
            Nuitka - Executable Compiler
            ------------
            Icon Used:
            ------------
            Icon by Freepik: https://www.flaticon.com/free-icon/tic-tac-toe_103227?related_id=103227&origin=search
            ------------
            Coded by OjanRN
            Github: https://github.com/OjanRN/
            ------------
            """)
            continue
        else:
            print("Wrong Input")
    


def mainmenu():
    maintitle = text2art("Net Tac Toe")
    print(maintitle)
    print("\n")
    print("[1] | Start Game")
    print("[2] | Settings")
    print("[3] | Exit")
    print("\n")
    while True:
        print("\n")
        menuInput = input("Menu Select: ")
        if menuInput == "1":
            startgame()
        elif menuInput == "2":
            settings()
        elif menuInput == "3":
            break #
        else:
            print("Wrong Input")
            continue


maintitle = text2art("Net Tac Toe")
tw(maintitle)
print("\n")
print("[1] | Start Game")
print("[2] | Settings")
print("[3] | Exit")
print("\n")
while True:
    print("\n")
    menuInput = input("Menu Select: ")
    if menuInput == "1":
        startgame()
    elif menuInput == "2":
        settings()
    elif menuInput == "3":
        break #
    else:
        print("Wrong Input")
        continue


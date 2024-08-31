"""
Joey Harper
2024 08 28
Slot Machine
"""
#MY own version that doesn't follow class but moves along in my free time.
import random
import time

bankRoll = 100


def gameLoop():
    leave = input("Would you like to play again? Y/N ").upper()  
    if leave == "Y":
        placeBets()
    elif leave == "N":
        print("\nThanks for Play Come Back Again!!")
    else:
        print("\nInvalid Choice It's not that hard")
        gameLoop()

def bankRun(bankInfo):
    runToBank = input("Would you like to add funds? Y/N ").upper()
    if runToBank == "Y":
        amount = input("\nHow much would you like to add? Choose between 10 and 200: ")
        if int(amount) < 10 and int(amount) > 200:
            print("\nInvalid entry no money for you!")
            return bankInfo
        else:
            print("\nPlease provide me with your banking information!")
            time.sleep(2)
            print("\nJust kinding here's your \"cash\"\n")
            bankInfo += int(amount)
            return bankInfo
    else:
        return bankInfo

def placeBets():
    global bankRoll
    
    bet = 5

    melon = 0
    seven = 0
    bar = 0
    lemon = 0
    cherry = 0

    melonPay = 3
    sevenPay = 12
    barPay = 5
    cherryPay = 7

    #melon, 7, bar, lemon, cherry
    winnings = 0

    print("Spinning Sots...")
    time.sleep(1)
    
    bankRoll -= bet
    for i in range(1,4):
        slot1 = random.randint(1,1000)
        if slot1 >= 1 and slot1 <= 175:
            melon += 1
            print("Melon")
        elif slot1 >= 900:
            seven += 1
            print("7")
        elif slot1 >= 800 and slot1 <= 899:
            bar += 1
            print("bar")
        elif slot1 >= 325 and slot1 <= 500:
            lemon += 1
            print("lemon")
        elif slot1 >= 501 and slot1 <= 799:
            cherry += 1
            print("cherry")
        else:
            print("gap")
        time.sleep(.5)

    """for i in roll:
        if i == "Melon":
            melon += 1
        elif i == "7":
            seven += 1
        elif i == "Bar":
            bar += 1
        elif i == "Lemon":
            lemon += 1
        elif i == "Cherry":
            cherry += 1"""

    if melon >= 2:
        winnings = melon * melonPay
    elif seven >= 2:
        winnings = seven * sevenPay
    elif bar >= 2:
        winnings = bar * barPay
    elif lemon >= 2:
        winnings = lemon * melonPay
    elif cherry >= 2:
        winnings = cherry * cherryPay
        

    bankRoll +=winnings

    if winnings == 0:
        print("\nYou won NOTHING!! You get NOTHING!!!")
    else:
        print(f"\nYou won ${winnings}!!")
    print(f"You now have ${bankRoll}\n")
    #print(melon, seven, bar, lemon, cherry)
    
    if bankRoll <= 90:
        bankRoll = bankRun(bankRoll)
        print(f"Your current bank roll is {bankRoll} good luck!!\n")
    gameLoop()

placeBets()

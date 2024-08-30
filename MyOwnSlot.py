"""
Joey Harper
2024 08 28
Slot Machine
"""
#Program follows along in class
import random
import time

bankRoll = 100

def placeBets():
    global bankRoll
    bet = 5

    melon = 0
    seven = 0
    bar = 0
    lemon = 0
    cherry = 0

    melonPay = 5
    sevenPay = 20
    barPay = 10
    cherryPay = 15

    #melon, 7, bar, lemon, cherry
    roll = []
    winnings = 0

    print("Spinning Sots...")
    time.sleep(1)
    
    bankRoll -= bet
    for i in range(1,4):
        slot1 = random.randint(1,5)
        if slot1 == 1:
            roll.append("Melon")
            print("Melon")
        elif slot1 == 2:
            roll.append("7")
            print("7")
        elif slot1 == 3:
            roll.append("Bar")
            print("bar")
        elif slot1 == 4:
            roll.append("Lemon")
            print("lemon")
        elif slot1 == 5:
            roll.append("Cherry")
            print("cherry")    

    for i in roll:
        if i == "Melon":
            melon += 1
        elif i == "7":
            seven += 1
        elif i == "Bar":
            bar += 1
        elif i == "Lemon":
            lemon += 1
        elif i == "Cherry":
            cherry += 1

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
    print(roll)
    if winnings == 0:
        print("\nYou won NOTHING!! You get NOTHING!!!")
    else:
        print(f"\nYou won ${winnings}!!")
    print(f"You now have ${bankRoll}\n")
    #print(melon, seven, bar, lemon, cherry)
    

    def gameLoop():
        leave = input("Would you like to play again? Y/N ").upper()  
        if leave == "Y":
            placeBets()
        elif leave == "N":
            print("\nThanks for Play Come Back Again!!")
        else:
            print("Invalid Choice It's not that hard")
            gameLoop()
    gameLoop()

placeBets()

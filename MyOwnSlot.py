"""
Joey Harper
2024 08 28
Slot Machine
"""
#MY own version that doesn't follow class but moves along in my free time.
import random
import time

#This is a class for various escapement values
class escape:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CLEAR ='\x1b[2K'
   UP ='\033[1A'

bankRoll = 100

#Game loop asks if you want to keep play then loops you back into the game.
def gameLoop():
    global bankRoll
    if bankRoll > 50:
        leave = input("\nWould you like to play again? Y/N ").upper() 
    elif bankRoll <= 50:
        G = escape.BLUE + "G" + escape.END
        A = escape.CYAN + "A" + escape.END
        Q = escape.PURPLE + "Q" + escape.END
        leave = input(f"""
        Having a rough time huh? You can choose to go on or to add funds.
        ({G})o On or
        ({A})dd Funds or
        ({Q})uit if your ready to leave
        """).upper()
    if leave == "Y" or leave == "G":
        placeBets()
    elif leave == "N" or leave == "Q":
        bankRollC = escape.GREEN + escape.UNDERLINE + escape.BOLD + str(bankRoll) + escape.END
        print(f"\nHere's your money, I guess. ${bankRollC} At least you have some left!")
        print("\nThanks for Playing, Come Back Again!!")
    elif leave == "A":
        bankRoll = bankRun(bankRoll)
        bankRollC = escape.RED + escape.BOLD + escape.UNDERLINE + str(bankRoll) + escape.END
        print(f"Your current bank roll is ${bankRollC} good luck!!\n")
        gameLoop()
    else:
        print("\nInvalid Choice It's not that hard")
        gameLoop()

#Bank run allows a player to "purchase" more money to play with and is propted to the player when their money is below $50. There is a set amount you can add 10-200, if you make and invalid entry you get nothing.
def bankRun(bankInfo):
    amount = input("\nHow much would you like to add? Choose between 10 and 200: ")
    dumb = escape.BOLD + escape.RED +"DUMBY" + escape.END
    try:
        int(amount)
    except ValueError:
        print(f"\nHey that's not a number {dumb}!\n")
        return bankInfo
    if amount >= 10 and int(amount) <= 200:
        print("\nPlease provide me with your banking information!\n")
        time.sleep(2)
        print("Just kinding here's your \"cash\"\n")
        bankInfo += int(amount)
        return bankInfo
    else:
        print("Invalid entry no money for you!\n")
        return bankInfo


#This is the main game that rolls random numbers and associates those with the reel items.
def placeBets():
    global bankRoll  
    bet = 5
    #These are all the various variables :D.
    melon = 0
    seven = 0
    bar = 0
    lemon = 0
    cherry = 0
    reelFill = ["melon", "seven", "bar", "lemon", "cherry"]
    #These are styling for the reel items so I can add some escape to the console
    melonStyle = escape.GREEN + "(" + escape.END + escape.CYAN + "M" + escape.END + escape.GREEN + ")" + escape.END
    sevenStyle = "[" + escape.RED + escape.BOLD + "7" + escape.END + "]"
    barStyle = escape.BLUE + "---" + escape.END
    cherryStyle = escape.RED + escape.BOLD + "o" + escape.END + escape.GREEN + "^" + escape.END + escape.RED + escape.BOLD + "o" + escape.END
    lemonStyle = escape.YELLOW + escape.BOLD + "{7}" + escape.END
    
    reelFill2 = [melonStyle, sevenStyle, barStyle, lemonStyle, cherryStyle]
    winReel = []

#These are all payout values
    melonPay = 3
    sevenPay = 12
    barPay = 5
    cherryPay = 7

    winnings = 0
    
    bankRoll -= bet
    
    #This bit picks a random number 3 times and adds 1 to the chosen items variable for use in payout calculation.
    for i in range(1,4):
        slot1 = random.randint(1,1000)
        if slot1 >= 1 and slot1 <= 150:
            melon += 1
            winReel.append(reelFill[0])
        elif slot1 >= 900:
            seven += 1
            winReel.append(reelFill[1])
        elif slot1 >= 800 and slot1 <= 899:
            bar += 1
            winReel.append(reelFill[2])
        elif slot1 >= 350 and slot1 <= 500:
            lemon += 1
            winReel.append(reelFill[3])
        elif slot1 >= 501 and slot1 <= 699:
            cherry += 1
            winReel.append(reelFill[4])
        else:
            winReel.append("Gap")
        
    #This bit spins your reels and prints out the final reel based on the out put from above.
    print("\n")
    counter = 0
    num = .15
    for i in range(6):
        if counter == 5:
            num = .6
        for i in range(5):
            print(reelFill2[i], reelFill2[-i], reelFill2[i])
            time.sleep(num)
            print(escape.UP, end=escape.CLEAR)
        counter += 1
        
    print("\n" + winReel[0], winReel[1], winReel[2] + "\n")

#Here we check for winning payouts atm it's just 2 or more gets multiplied by an arbitrary item value.
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
        
#Then add them to the bankroll.
    bankRoll +=winnings

#This is your winning information message either you won or you didn't. If you did you get told how much if not it mocks you Willy Wonka style.
    nothing = escape.RED + escape.BOLD + "NOTHING!!!" + escape.END
    if winnings == 0:
        print(f"You won {nothing} You get {nothing}\n")
    elif winnings > 0:
        winC = escape.GREEN + escape.BOLD + escape.UNDERLINE + str(winnings) + escape.END
        winC = '\033[1m' + '\033[4m' + winC + '\033[0m'
        print(f"You won ${winC}!!\n")
    bankRollC = escape.RED + escape.BOLD + escape.UNDERLINE + str(bankRoll) + escape.END
    print(f"You now have ${bankRollC}\n")
    gameLoop()
    #print(melon, seven, bar, lemon, cherry)

#This bit cheks if your bank drops to 50 and prompts you the option to add funds.  
    if bankRoll < bet:
        print("\nSorry Loser you're outa Cash!!")
    
#Of course this guy starts us off by immediately running the game.
placeBets()

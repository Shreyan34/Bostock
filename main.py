import random # import dependencies

# Define ranks and suits
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Generate the full deck using a list comprehension
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# define the main loop
def mainLoop():
   
    # use python's built-in function to shuffle the deck of cards in random
    random.shuffle(deck)

    # bet -- human or computer's choice
    choice = int(input("Type 1 to make a bet yourself.\nType any other number to let the computer make the bet.\n"))
    bet = 0 # initialise the 'bet' variable
    if(choice == 1): bet = int(input("Type your bet:"))
    else: bet = random.randint(14,34) # find a random sum to act as a bet

    print(f"Sum to bet: {bet}") # print the sum to bet

    # draw the cards
    d1 = int(input("First Card: "))
    d2 = int(input("Second Card: "))
    d3 = int(input("Third Card: "))
    d4 = int(input("Fourth Card: "))
    print("") # for neatness

    # check if two cards are same
    if(d1 == d2 or d1 == d3 or d1 == d4 or d2 == d3 or d2 == d4 or d3 == d4): 
        print("No two cards can be same!")
        pass

    # check boundaries
    if(d1 > 52 or d2 > 52 or d3 > 52 or d4 > 52):
        print("Invalid input!")
        pass

    # find the cards
    f1 = deck[d1-1] 
    f2 = deck[d2-1]
    f3 = deck[d3-1]
    f4 = deck[d4-1]

    # display the cards chosen
    print(f"First card chosen: {f1}") 
    print(f"Second card chosen: {f2}")
    print(f"Third card chosen: {f3}")
    print(f"Fourth card chosen: {f4}")
    print("") # for neatness

    # get the first words
    firstLetter1 = f1.split()[0]
    firstLetter2 = f2.split()[0]
    firstLetter3 = f3.split()[0]
    firstLetter4 = f4.split()[0]

    # assign points to picture cards using dictionaries
    faceCardPoints = {
        "Queen": 15,
        "King": 10,
        "Jack": 5,
        "Ace": 5
    }

    # now, obtain the values
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0

    # check for face card points, else pass
    if(firstLetter1 != 'Queen' and firstLetter1 != 'King' and firstLetter1 != 'Jack' and firstLetter1 != 'Ace'):
        v1 = int(firstLetter1)
    else:
        v1 = faceCardPoints[firstLetter1]
    
    if(firstLetter2 != 'Queen' and firstLetter2 != 'King' and firstLetter2 != 'Jack' and firstLetter2 != 'Ace'):
        v2 = int(firstLetter2)
    else:
        v2 = faceCardPoints[firstLetter2]
    
    if(firstLetter3 != 'Queen' and firstLetter3 != 'King' and firstLetter3 != 'Jack' and firstLetter3 != 'Ace'):
        v3 = int(firstLetter3)
    else:
        v3 = faceCardPoints[firstLetter3]  

    if(firstLetter4 != 'Queen' and firstLetter4 != 'King' and firstLetter4 != 'Jack' and firstLetter4 != 'Ace'):
        v4 = int(firstLetter4)
    else:
        v4 = faceCardPoints[firstLetter4]  

    # print the values that the player gets
    print("You got the following values!")
    print(f"Value 1: {v1}")
    print(f"Value 2: {v2}") 
    print(f"Value 3: {v3}")
    print(f"Value 4: {v4}")
    print("") # for neatness

    sum = v1 + v2 + v3 + v4
    print(f"YOUR SUM: {sum}")
    if(sum>=bet):
        print("YOU HAVE WON!!!")
    else:
        print("OOPS!! Better luck next time!")
    

# print the rules of Bostock
print("==================================================================")
print("                             BOSTOCK (0.1)                        ")
print("                 created by Shreyan Kumar Mishra, 2025.           ")
print("==================================================================")
print("                             :RULES:                              \n")
print("Bostock is played with a standard 52-card deck (no jokers).")
print("Shuffle the deck at the start of each round.")
print("The computer (or dealer) sets a random bet between 14 and 34.")
print("The player chooses four distinct card positions (1–52).")
print("Reveal the chosen cards from the shuffled deck.")
print("Assign values: numbers = face value, Jack = 5, Queen = 15, King = 10, Ace = 5.")
print("Add up the four values to get the player’s sum.")
print("If sum ≥ bet, the player wins; otherwise, the player loses.")
print("Duplicate or invalid card positions are not allowed.")
print("Play multiple rounds; highest number of wins decides the champion.\n")
print("==================================================================")

mainLoop() # call the main loop of the game

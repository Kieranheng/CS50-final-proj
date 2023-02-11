import cs50
from random import shuffle

# preparation of deck
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']

def get_deck():

    return [[rank, suit] for rank in ranks for suit in suits]

# initialise earnings as 0 at start of game
earnings = 0

print("Welcome to Baccarat!")

while True:
# allow user to place bet
    while True:
        try:
            bet = int(input("Place your bet: "))
            if (0 < bet):
                break
        except ValueError:
            print("Invalid Bet!")

# deal cards to create hands
    deck = get_deck()
    shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    opponent_hand = [deck.pop(), deck.pop()]

# function to obtain value of card
    def card_value(card):
        # value on card is first element on card list
        rank = card[0]
        # if value on card is number
        if rank in range(2,11):
            value = rank
        # if ace card, value is 1
        elif rank == 'ACE':
            value = 1
        # else card must be picture card, value is 10
        else:
            value = 10
        return value

    # initialise scores of player and opponent hands and player earnings
    playervalue = 0
    oppvalue = 0

    # obtain scores of player and opponent hands
    for i in range(2):
        x = card_value(player_hand[i])
        playervalue += x
        y = card_value(opponent_hand[i])
        oppvalue += y

    # get last digit of added up score for baccarat score
    playervalue = playervalue % 10
    oppvalue = oppvalue % 10
    # show player hand and score to user
    print("\nYour hand is")
    print(player_hand)
    print("Your score is " + str(playervalue))
    # in case of natural (8 or 9), auto win unless other player has a better hand
    if playervalue > 7 and playervalue > oppvalue:
        # since game ends immediately, show opponent hand to user
        print("\nOpponent hand is")
        print(opponent_hand)
        print("Opponent score is " + str(oppvalue))
        print("\nYou win!")
        # if same suit or same numbers, earnings doubled
        if player_hand[0][0] == player_hand[1][0] or player_hand[0][1] == player_hand[1][1]:
            earnings = earnings + bet*2
        else:
            earnings = earnings + bet
        print("\nCurrent earnings: " + str(earnings))
    elif playervalue > 7 and playervalue == oppvalue:
        print("\nOpponent hand is")
        print(opponent_hand)
        print("Opponent score is " + str(oppvalue))
        print("\nTie!")
        print("\nCurrent earnings: " + str(earnings))
    elif oppvalue > 7 and oppvalue > playervalue:
        print("\nOpponent hand is")
        print(opponent_hand)
        print("Opponent score is " + str(oppvalue))
        print("\nYou lose!")
        if opponent_hand[0][0] == opponent_hand[1][0] or opponent_hand[0][1] == opponent_hand[1][1]:
            earnings = earnings - bet*2
        else:
            earnings = earnings - bet
        print("\nCurrent earnings: " + str(earnings))
    # if no natural first hands, continue game
    elif playervalue < 8 and oppvalue < 8:
        # ask user if he/she wants to draw a card or not
        hit = input("Do you want to hit or stand? \n" )
        # if hit, add card to player hand
        if hit.upper() == "HIT":
            player_hand.append(deck.pop())
            playervalue = playervalue + card_value(player_hand[2])
            playervalue = playervalue % 10
        # if stand, no change
        elif hit.upper() == "STAND":
            playervalue = playervalue % 10
        # ensure user only enters "hit" or "stand"
        else:
            print("Enter Hit or Stand")
    # CPU opponent hits at every score below 5
        if oppvalue < 5:
            opponent_hand.append(deck.pop())
            oppvalue = oppvalue + card_value(opponent_hand[2])
            oppvalue = oppvalue % 10
    # after player and opponent have chosen whether to hit or stand, open cards
        print("\nYour hand is")
        print(player_hand)
        print("Your score: " + str(playervalue))

        print("\nOpponent's hand is")
        print(opponent_hand)
        print("Opponent's score: " + str(oppvalue))

    # determine eventual winner of game
        if playervalue > oppvalue:
            print("\nYou win!")
            if len(player_hand) == 2:
                #if same suit or same number, winnings doubled/tripled, depending on how many cards
                if player_hand[0][0] == player_hand[1][0] or player_hand[0][1] == player_hand[1][1]:
                    earnings = earnings + bet*2
                else:
                    earnings = earnings + bet
            elif len(player_hand) == 3:
                if player_hand[0][0] == player_hand[1][0] == player_hand[2][0] or player_hand[0][1] == player_hand[1][1] == player_hand[2][1]:
                    earnings = earnings + bet*3
                else:
                    earnings = earnings + bet

        elif oppvalue > playervalue:
            print("\nYou lose!")
            if len(opponent_hand) == 2:
                if opponent_hand[0][0] == opponent_hand[1][0] or opponent_hand[0][1] == opponent_hand[1][1]:
                    earnings = earnings - bet*2
                else:
                    earnings = earnings - bet
            elif len(opponent_hand) == 3:
                if opponent_hand[0][0] == opponent_hand[1][0] == opponent_hand[2][0] or opponent_hand[0][1] == opponent_hand[1][1] == opponent_hand[2][1]:
                    earnings = earnings - bet*3
                else:
                    earnings = earnings - bet
        # if player and opponent scores are the same, tie, no change
        else:
            print("\nTie!")
        # show user how much he/she has earned
        print("\nCurrent earnings: " + str(earnings))

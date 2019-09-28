#BLACKJACK MILESTONE PROJECT

import random

class Cards():
    '''
    Establish a set of cards
    Reset and shuffle those cards
    Establish Ace as 1 or 11
    Adding an update
    '''
    deckkey = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']*4
    deckval = [2,3,4,5,6,7,8,9,10,10,10,10,[1,11]]*4
    deckdict = dict(zip(deckkey,deckval)) #zipping the keys, values into a dict
    Ace = [1,11]
    NewKing = 0

    def __init__(self,game):
        self.game = game

    def __str__(self):
        return f'the card set is {self.deckkey} and the dict ' \
               f'\n is {self.deckdict}'

    def __len__(self):
        return len(self.deckkey)

    def shuffle(self):
        return random.shuffle(self.deckkey)

# a = Cards.deckdict
# print(a['King'])
# the other way to lookup values in a dictionary is just to call dict[key]



class Player():
    '''
    Create bank account
    Player can bet up to bank account
    Add a win to bank account
    '''
    def __init__(self,name,chips):
        #default arguments must be last
        self.name = name
        self.chips = chips

    def __str__(self):
        return f'Player is {self.name} and they have {self.chips} to bet'

    def bet_amt (self):
        while True:
            if self.chips == 0:
                print('You are out of money')
                amount = 0
                break
            try:
                amount = int(input(f'{p1.name}, place your bet: '))
            except:
                print(f'Whoops, enter a number between 1-{self.chips}')
                continue
            if amount > self.chips:
                print(f'You only have {self.chips} to bet, try again')
                continue
            else:
                self.chips = self.chips - amount
                print(f'You bet {amount}, you have {self.chips} left')
                break
        return amount

    def win_loss(self, amount):
        try:
            if push == True:
                self.chips = self.chips + int(amount)
                print('PUSH')
        except:
            print('\n')
        if win == True:
            self.chips = self.chips + int(amount)*2
            print('WINNER!')
        else:
            print('YOU LOST')
        return print(f'you now have {self.chips}!')

def deal():
    first_card = livedeck[0]
    second_card = livedeck[1]
    third_card = livedeck[2]
    fourth_card = livedeck[3]
    player_card_list = [first_card, third_card]
    dealer_card_list = [second_card, fourth_card]
    return player_card_list, dealer_card_list, second_card, fourth_card

def player_value():
    player_val = 0
    player_val_max = 0
    player_val_min = 0
    if 'Ace' not in player_card_list:
        for i in range(0,len(player_card_list)):
            player_val = player_val + livedeckdict.get(player_card_list[i], 0)
        print(f'Cards: {player_card_list[0]} and '
              f'{player_card_list[1]}. You are showing {player_val}')
    else:
        for i in range(0,len(player_card_list)):
            if player_card_list[i] == 'Ace':
                player_val_max = player_val_max + acelist[1]
                player_val_min = player_val_min + acelist[0]
            else:
                player_val_max = player_val_max + livedeckdict.get(player_card_list[i], 0)
                player_val_min = player_val_min + livedeckdict.get(player_card_list[i], 0)
        print(f'Your cards: {player_card_list}')
        print(f'You are showing {player_val_max} or {player_val_min}')
    return (player_val, player_val_max, player_val_min)

def check_bust(player_card_list, player_val, player_val_min):
    bust = False
    if 'Ace' not in player_card_list and player_val > 21:
        bust = True
    elif player_val_min > 21:
        bust = True
    else:
        bust = False
    return bust

def hit_or_stay():
    playaction = True
    cardcount = 4
    bust = False
    while bust == False:
        action = input('Hit(h) or Stay?(s): \n')
        if action == 'h':
            print(f'Hit: {livedeck[cardcount]}\n')
            player_card_list.append(livedeck[cardcount])
            player_val, player_val_max, player_val_min = player_value()
            # print(player_card_list)
            cardcount += 1
            # print(cardcount)
            if check_bust(player_card_list, player_val, player_val_min) == True:
                bust = True
                player_card_list.append('BUST')
                print(f'{player_value()}, YOU BUSTED!')
                break
            else:
                continue
        elif action == 's':
            player_val, player_val_max, player_val_min = player_value()
            break
        else:
            print("Whoops, you must enter 'h' for hit or 's' for stay")
    return player_val, player_val_min, bust, cardcount
# print(f'this was the last card: {ending_card_count}')
# print(f'Total cards: {len(player_card_list)}')
# print(player_card_list[len(player_card_list)-1])

#Another way to check bust
# if player_card_list[len(player_card_list)-1] == "BUST":
#     youbusted = True
#     print('you busted')
# else:
#     youbusted = False
#     print('Monkey'+'\n'*10)
#
# print(f'Dealer turns over a {second_card}')
# print(dealer_card_list)

def dealer_check_bust(dealer_card_list, dealer_val, dealer_val_min):
    bust = False
    if 'Ace' not in dealer_card_list and dealer_val > 21:
        bust = True
    elif dealer_val_min > 21:
        bust = True
    else:
        bust = False
    return bust


def dealer_value():
    dealer_val = 0
    dealer_val_max = 0
    dealer_val_min = 0
    if 'Ace' not in dealer_card_list:
        for i in range(0,len(dealer_card_list)):
            dealer_val = dealer_val + livedeckdict.get(dealer_card_list[i], 0)
        print(f'\nDealer is showing {dealer_val}')
    else:
        for i in range(0,len(dealer_card_list)):
            if dealer_card_list[i] == 'Ace':
                dealer_val_max = dealer_val_max + acelist[1]
                dealer_val_min = dealer_val_min + acelist[0]
            else:
                dealer_val_max = dealer_val_max + livedeckdict.get(dealer_card_list[i], 0)
                dealer_val_min = dealer_val_min + livedeckdict.get(dealer_card_list[i], 0)
        print(f'\nDealer showing {dealer_val_max} or {dealer_val_min}')
    return dealer_val, dealer_val_max, dealer_val_min


# print(f'dealer_val = {dealer_val}')
# print(f'dealer_val_max = {dealer_val_max}')
# print(f'dealer_val_min = {dealer_val_min}')

def dealer_hit_or_stay():
    cardcount = ending_card_count
    dealer_bust = False
    print('\nDEALER TURN...')
    while dealer_bust == False:
        dealer_val, dealer_val_max, dealer_val_min = dealer_value()
        if dealer_val < 17 and dealer_val_min < 17:
            print(f'Dealer hits: {livedeck[cardcount]}')
            dealer_card_list.append(livedeck[cardcount])
            print(dealer_card_list)
            dealer_val, dealer_val_max, dealer_val_min = dealer_value()
            cardcount += 1
            # print(cardcount)
        else:
            print('Dealer Stays')
            break
        if dealer_check_bust(dealer_card_list, dealer_val, dealer_val_min) == True:
            dealer_bust = True
            dealer_card_list.append('BUST')
            print(f'{dealer_value()}, DEALER BUSTS')
            break
        else:
            continue
    return dealer_val, dealer_val_min, dealer_bust

def win_check():
    win = False
    push = False
    if player_val_max > 21:
        check_value_player = max(player_val, player_val_min)
    else:
        check_value_player = max(player_val, player_val_max, player_val_min)
    if dealer_val_max > 21:
        check_value_dealer = max(dealer_val, dealer_val_min)
    else:
        check_value_dealer = max(dealer_val, dealer_val_max, dealer_val_min)
    if check_value_player == check_value_dealer:
         print(f'\nDealer has {check_value_dealer} and you have {check_value_player}, push')
         push = True
    elif check_value_player > check_value_dealer:
        win = True
        print(f'\nDealer has {check_value_dealer} and you have {check_value_player}, you win')
    else:
        win = False
        print(f'\nDealer has {check_value_dealer} and you have {check_value_player}, you lose')
    return check_value_player, check_value_dealer, push, win



def play_again():
    play_again = input('\nPlay again? Y or N: ')
    if play_again == 'Y':
        bet_again = True
    else:
        bet_again = False
    return bet_again



#GAMEPLAY
replay = True # setting replay default to true
a = Cards('Blackjack') # assigning card values to variable a
acelist = Cards.Ace #assigning multiple values of ace to variable acelist
p1 = Player('Jeremy', 200) #establishing an initial player and bank account and assinging to var p1
print(p1) # printing the details using special __str___
while replay == True:
    a.shuffle() #shuffling the cards using the random function
    #print(f'the shuffled card set is {a}') # printing the list of shuffled cards
    livedeck = a.deckkey # initializing a list of shuffled cards (keys) and assigning to var livedeckkey
    livedeckval = a.deckval # initializing a list of shuffled cards (vals) as assigning to var livedeckval
    livedeckdict = a.deckdict # initializing a dictionary of shuffled cards as assigning to var livedeckdict
    bet = p1.bet_amt() # assinging bet method, which prompts a user for #, to var bet
    if bet == 0:
        print('game over')
        break
    player_card_list, dealer_card_list, second_card, fourth_card = deal()  # running the method deal(), and unpacking the tuple
    print(f'\nDealer is showing {fourth_card}\n') # printing the upcard
    player_val, player_val_max, player_val_min = player_value() # running the method player_value, which takes the keys and turns them into values, and then unpacks the tuple
    busted = check_bust(player_card_list, player_val, player_val_min) # assinging the check_bust method to var: busted
    player_val, player_val_min, bust, cardcount = hit_or_stay() #running hit_or_stay method and unpacking the tuple of new player values
    print(player_card_list) #printing the new player card list
    ending_card_count = cardcount # initializing new variable of ending card count to then run the dealer value
    if bust == True:
        win = False  # determines if there was a win or push, and unpacks the tuple
        p1.win_loss(bet)  # adjusts the bank account based on what happened
    else:
        dealer_val, dealer_val_max, dealer_val_min = dealer_value() #  running the method dealer_value, which takes the keys and turns them into values, and then unpacks the tuple
        dealer_val, dealer_val_min, dealer_bust = dealer_hit_or_stay() # runs the dealer hit_or_stay method and unpacks the tuple
        print(dealer_card_list) #prints the new card list
        if dealer_bust == True:
            print('DEALER BUSTS')
            win = True # determines if there was a win or push, and unpacks the tuple
            p1.win_loss(bet) #adjusts the bank account based on what happened
        else:
            check_value_player, check_value_dealer, push, win = win_check()  # determines if there was a win or push, and unpacks the tuple
            p1.win_loss(bet)  # adjusts the bank account based on what happened
    play = play_again()
    if play == False:
        print('See you next time and good luck!')
        replay = False
        break
    else:
        continue


# '''
#
#
#
# Player Action
#
# View cards and count
# Player can choose between hit or stay
# Determine if cards are BUST
# Prompt to restart the game if BUST
#
# Dealer Action
# Show uncovered card
# Deal until reach 17
# Determine if cards are BUST
# Take or give money equal to bet
# Prompt to restart the game if BUST
#
# If no Bust: Determine Winner
# Take or give money equal to bet
#
# '''
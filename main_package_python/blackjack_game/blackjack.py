import random

suits = ('Heart','Diamond','Spade','Club')

ranks = ('Two','Three','Four','Five','Six','Seven',
        
        'Eight','Nine','Ten','Jack','Queen','King','Ace'
         )
# here jack ,queen and king have same priority of 10 
value = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11 }

###################################################################

class Card:
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        
###################################################################

class Deck:
    
    def __init__(self):
        self.all_cards = []  # start with an empty list
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank)) # build Card objects and add them to the list
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def __str__(self):
        deck_comp = ' '   # start with an empty string
        for card in self.all_cards:
            deck_comp += '\n'+card.__str__()  # add each Card object's print string
        return 'The deck has' +deck_comp
    
    def deal(self):
        
        single_card =self.all_cards.pop()
        return single_card
       
####################################################################

class Hand():
    
    def __init__(self,):
        self.aces = 0       # add an attribute to keep track of aces
        self.value = 0      # we have actually here add cards by hepling this 
        self.cards = []   # at very start cards will be zero
   
    def add_cards(self,card):
        #card passed in
        # from Deck.deal() ---->>> single_card(suit,rank)
        self.cards.append(card)
        self.value += value[card.rank] # we have actually find the sum of value of cards 
         # we know if value >21 so this values whovever has hand will be lost
            
        #IF CARD WILL BE ACE (track aces)
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        
        # IF sum is > 21 and card is still ace then change my ace to be an 1 instead of 11  
        while self.value > 21 and self.aces > 0:
            
            self.value -= 10
            self.aces -= 1
        
    
####################################################################

class Chips:
    
    def __init__(self,total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input i.e such as intead of 100 chips u can set 1000 ,45000 anything u want
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

####################################################################

def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("How many chips would you like to bet : "))
        except:
            print("Sorry, please provide an integer")
            continue
            
        else:
            if chips.bet > chips.total:
                print("Hey you don't have enough chips! you have {}".format(chips.total))
                
            else:
                break
            
####################################################################

# this will call if input will be 'h'  and hand is instance of Hand class so u can grab all attributes like add_cards ,adjusr_for_ace
def hit(deck,hand):
    
    
    hand.add_cards(deck.deal())
    hand.adjust_for_ace()
        
####################################################################

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        # u can write while loop like while not in ['h' , 's'] also here or try and except
        # see how we validate input new here
        x = ' '
        while x not in ['h' ,'s']:
            x = input("Hit or stand? enter 'h' or 's' : ")
            
            if x not in ['h' ,'s']:
                print("Sorry, Please enter 'h' or 's': ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print("player's stand dealer's turn")
            playing = False  # this playing is same for while loop in actual game code while playing: wala bcoz after hit 's' playing = false and will come out of that while loop so its necessary here same global playing
            
        else:
            print("sorry, you have enter wrong input ,please eneter 'h' or 's'")
            continue
        
        break
            
#####################################################################

def show_some(player,dealer):   # here we passed player_hand and dealer_hand i.e instance
    print("\nDealer's Hand:")
    print(" <card hidden>")  # 1st will be hidden
    print('',dealer.cards[1]) # here we show 2nd card of dealer only this .cards is from hand calss which is for dealer hand cards available  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')   # here we willshow all players cards at separate line
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')   # we will show all cards of dealer
    print("Dealer's Hand =",dealer.value)  # its total value
    print("\nPlayer's Hand:", *player.cards, sep='\n ') # we will show all cards of player
    print("Player's Hand =",player.value)  #player's total value
    
#####################################################################

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet() 

def player_wins(player,dealer,chips):
    print("PlAYER WINS!")
    chips.win_bet() # this is for player hand

def dealer_busts(player,dealer,chips):
    print("PlAYER WINS! DEALER BUSTED!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player tie! PUSH")
    
######################################################################

# AND NOW ON GAME

playing = True
while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK GAME!")

    
    # Create & shuffle the deck, deal two cards to each player
    
    deck = Deck()
    deck.shuffle()
    
    # deal two cards so two times add by dealing
    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    # same for dealer
    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    
    
    # Set up the Player's chips
    player_chips = Chips()  # by default 100 chips  # u can change

    
    # Prompt the Player for their bet
    
    take_bet(player_chips)   # humne yaha par satta lagate hain about money it should be less than chips.total money i.e 100
    # ye call hoga aur dekhega input lega aur cheack karega ki tumhne less value hi game main lagaya hain na than total in terem of chips
    # money means here chips
    # and if u win thae match win_bet call hoga from Chips class and total main jitna paisa lagaya that vo add joga 
    # noww maine paisa to lagaya dealer ke sath anhi cards show karne ke bolne ka hain dealer ko but 1 card will be hiiden
    
    
    # Show cards (but keep one dealer card hidden)
    # here show_some will be called and 2nd dealer card will be shown only and 1st will be hidden and will show all cards of player_hand
    show_some(player_hand,dealer_hand)   

    # now game will be start we have created deck shuufle it , we have created player_hand,dealer_hand ,humne game ke liye chips bhi decidekiye
    # by taking input of chips by calling take_bet , and show_some cards to player and dealer ho gaya now time for playing turns to hit and stand
    while playing:  # recall this variable from our hit_or_stand function
        
        # this turn is of player_hand
        # Prompt for Player to Hit or Stand
        # so this will call hit_or_stand after than it checks 'h' or 's' if 'h' it will call hit method then it grabs method of hand class add_cards and adjust_for_ace so see flow of calling 
        hit_or_stand(deck,player_hand) # we passed deck for deal() from all cards available to pop one card and player_hand for use when called hit method to grab methods of all Hand class 
        
        # Show cards (but keep one dealer card hidden)
        # here also after hit or stand we willshow some_cards i.e one hidden card of dealer else all visible
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        # u hava hot the cards and cards will added but if while adding cards if its value exceeds 21 player_hand will busted so we will call player_bust method and break the loop
        if player_hand.value > 21:   # here this .value is in Hand class in add_cards method bcoz we call by instance i.e player_hand and after hit card the self.value will be added every timme it ill update everytime see hand class
            player_busts(player_hand,dealer_hand,player_chips)  # so u have busted so calling lose_bet from player_busts bcoz total will be decrement by chips.bet which u have gave input when u called the take_bet so its all connectivity see properly
            
            break
            
        # from this while loop when u will come out there is 2 cases:
        # 1) if u hit and suddenly value goes > 21 it will break
        # 2) if ur input is 's ' i.e stand playing will become False and will come out of this loop see hit_or_stand that there is also same global variable playing so it should be same


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    # now plaer_hand trns completed that he hits 's' and come out while loop now dealer's turn
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:   # whenever dealer value will be < 17 hit      
            hit(deck,dealer_hand)
            
        
            
        # here for delaer turn there is no problem to hidden so show_all cards and here value is also shown
        # Show all cards
        show_all(player_hand,dealer_hand)
        
    
        # Run different winning scenarios
        if dealer_hand.value > 21:  # in this nested if origirn if means player value is < 21 but suddenly dealer value goes over 21 he will busted so caleed delaer busts method
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)   #this is for tie
            
        
    # at last we will show total chips of plaer_hand
    # Inform Player of their chips total
    print('\n player has total chips at {}'.format(player_chips.total))
    
    # Ask to play again
    # new cahnge here see how we validate input
    new_game = 'wrong'
    while new_game not in ['y' , 'n']:
        new_game = input("Would you like to play another hand 'y' or 'n': ")

        if new_game not in ['y' , 'n']:
            print("Sorry, your input was wrong! please enter 'y' or'n'")

    if new_game[0].lower() == 'y':

        playing = True  # this playing is of outer that was declared at very 1st line for while Treu: game
        continue

    elif new_game[0].lower() == 'n':

        playing = False  # this will break the outwer while loop so we will give some tahnks msg for playing 
        print("Thanks for playing")
        break




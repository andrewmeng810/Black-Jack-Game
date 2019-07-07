#!/usr/bin/env python
# coding: utf-8

# # Blackjack Game
#

# ## Game Play
# To play a hand of Blackjack the following steps must be followed:
# 1. Create a deck of 52 cards
# 2. Shuffle the deck
# 3. Ask the Player for their bet
# 4. Make sure that the Player's bet does not exceed their available chips
# 5. Deal two cards to the Dealer and two cards to the Player
# 6. Show only one of the Dealer's cards, the other remains hidden
# 7. Show both of the Player's cards
# 8. Ask the Player if they wish to Hit, and take another card
# 9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# 10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# 11. Determine the winner and adjust the Player's chips accordingly
# 12. Ask the Player if they'd like to play again

# ## Playing Cards
# A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in your program, you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.

# ## The Game
# ### Imports and Global Variables
# ** Step 1: Import the random module. This will be used to shuffle the deck prior to dealing. Then, declare variables to store suits, ranks and values. You can develop your own system, or copy ours below. Finally, declare a Boolean value to be used to control <code>while</code> loops. This is a common practice used to control the flow of the game.**
#
#     suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#     ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#     values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
#              'Queen':10, 'King':10, 'Ace':11}

# In[12]:


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


# ### Class Definitions
# Consider making a Card class where each Card object has a suit and a rank, then a Deck class to hold all 52 Card objects, and can be shuffled, and finally a Hand class that holds those Cards that have been dealt to each player from the Deck.

# **Step 2: Create a Card Class**<br>
# A Card object really only needs two attributes: suit and rank. You might add an attribute for "value" - we chose to handle value later when developing our Hand class.<br>In addition to the Card's \_\_init\_\_ method, consider adding a \_\_str\_\_ method that, when asked to print a Card, returns a string in the form "Two of Hearts"

# In[13]:


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


# **Step 3: Create a Deck Class**<br>
# Here we might store 52 card objects in a list that can later be shuffled. First, though, we need to *instantiate* all 52 unique card objects and add them to our list. So long as the Card class definition appears in our code, we can build Card objects inside our Deck \_\_init\_\_ method. Consider iterating over sequences of suits and ranks to build out each card. This might appear inside a Deck class \_\_init\_\_ method:
#
#     for suit in suits:
#         for rank in ranks:
#
# In addition to an \_\_init\_\_ method we'll want to add methods to shuffle our deck, and to deal out cards during gameplay.<br><br>
# OPTIONAL: We may never need to print the contents of the deck during gameplay, but having the ability to see the cards inside it may help troubleshoot any problems that occur during development. With this in mind, consider adding a \_\_str\_\_ method to the class definition.

# In[14]:


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_com = ''
        for card in self.deck:
            return '{}\n'.format(card.__str__())

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# TESTING: Just to see that everything works so far, let's see what our Deck looks like!

# In[15]:



# **Step 4: Create a Hand Class**<br>
# In addition to holding Card objects dealt from the Deck, the Hand class may be used to calculate the value of those cards using the values dictionary defined above. It may also need to adjust for the value of Aces when appropriate.

# In[16]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if values[card.rank] == 'Ace':
            self.aces += 1



    def adjust_for_ace(self):

        # adjust when player hand has more than 1 ace, and total value greater than 21
        while self.aces > 0 and self.values > 21:
            self.value -= 10
            self.aces -=1






# **Step 5: Create a Chips Class**<br>
# In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings. This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!

# In[17]:


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# ### Function Defintions
# A lot of steps are going to be repetitive. That's where functions come in! The following steps are guidelines - add or remove functions as needed in your own program.

# **Step 6: Write a function for taking bets**<br>
# Since we're asking the user for an integer value, this would be a good place to use <code>try</code>/<code>except</code>. Remember to check that a Player's bet can be covered by their available chips.

# In[18]:


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please provide your bet: '))
        except:
            print('Please provide a valid integer.')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough credits. Your current balance is: {}'.format(chips.total))
            else:
                break   # end the loop, and take the bet from player



# **Step 7: Write a function for taking hits**<br>
# Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.

# In[33]:


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()      # hit the card, and adjust the aces when needed


# **Step 8: Write a function prompting the Player to Hit or Stand**<br>
# This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.<br>
# If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a <code>while</code> loop later on in our code.

# In[34]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        answer = input('Would you like to hit or stand? h/s')

        if answer[0].lower() == 'h':
            hit(deck, hand)
        elif answer[0].lower() == 's':
            print("Player choose to stand, Dealer's turn")
            playing = False
        else:
            print('Please choose either h or s.')
            continue
        break


# **Step 9: Write functions to display cards**<br>
# When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible. At the end of the hand all cards are shown, and you may want to show each hand's total value. Write a function for each of these scenarios.

# In[46]:


def show_some(player,dealer):
    print("Dealer's hand:")
    print(' <HIDDEN CARD>')
    print(dealer.cards[1])
    print('--------------------------')
    print("Player's hand: ", *player.cards, sep= '\n ')

def show_all(player,dealer):
    print("Dealer's hand:", *dealer.cards, sep= '\n ')
    print("Dealer's hand value: {}".format(dealer.value))
    print('--------------------------')
    print("Player's hand: ", *player.cards, sep= '\n ')
    print("Player's hand value: {}".format(player.value))





# **Step 10: Write functions to handle end of game scenarios**<br>
# Remember to pass player's hand, dealer's hand and chips as needed.

# In[44]:


def player_busts(player, dealer, chips):
    print('Player busts! Player loses all the bet')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins the game! Player wins all the bet')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer busts! Player wins all the bet')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Deal wins the game! Player loses all the bet')
    chips.lose_bet()
def push(player, dealer, chips):
    print('Dealer and player tied.')



#  Now is the Game

while True:
    # Print an opening statement
    print('***********************************************')
    print('******** Welcome to the Black Jack Game *******')
    print('***********************************************')

    # Create & shuffle the deck, deal two cards to each player

    game_deck = Deck()
    game_deck.shuffle()    # shuffle the deck


    dealer_hand = Hand()
    player_hand = Hand()

    dealer_hand.add_card(game_deck.deal())
    dealer_hand.add_card(game_deck.deal())

    player_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())


    # Set up the Player's chips

    player_chips = Chips()


    # Show cards (but keep one dealer card hidden)

    show_some(player_hand, dealer_hand)


    # Prompt the Player for their bet
    take_bet(player_chips)


    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop

        while player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

    if player_hand.value <= 21:
        while dealer_hand.value <= 17:
            hit(game_deck, dealer_hand)

        # Show all cards

        show_all(player_hand, dealer_hand)

        # Run different winning scenarios

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand, player_chips)

    # Inform Player of their chips total
    print('--------------------------')
    print("Player's current balanace is: {}".format(player_chips.total))


    # Ask to play again

    new_game = input('Would you like to play another hand? y/n')
    if new_game[0].lower() == 'y':
        playing = True
        continue                      # continue the loop

    elif new_game[0].lower() == 'n':
        print('Thank you for playing!')
        break

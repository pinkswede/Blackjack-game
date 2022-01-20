#!/usr/bin/env python
# coding: utf-8

# In[81]:


import random

def draw_card():
    
    cards_hearts=[('1',1,'♥'),
               ('2',2,'♥'),
               ('3',3,'♥'),
               ('4',4,'♥'),
               ('5',5,'♥'),
               ('6',6,'♥'),
               ('7',7,'♥'),
               ('8',8,'♥'),
               ('9',9,'♥'),
               ('10',10,'♥'),
               ('J',10,'♥'),
               ('Q',10,'♥'),
               ('K',10,'♥')]
    cards_clubs=[('1',1,'♣'),
               ('2',2,'♣'),
               ('3',3,'♣'),
               ('4',4,'♣'),
               ('5',5,'♣'),
               ('6',6,'♣'),
               ('7',7,'♣'),
               ('8',8,'♣'),
               ('9',9,'♣'),
               ('10',10,'♣'),
               ('J',10,'♣'),
               ('Q',10,'♣'),
               ('K',10,'♣')]
    cards_spades=[('1',1,'♠'),
               ('2',2,'♠'),
               ('3',3,'♠'),
               ('4',4,'♠'),
               ('5',5,'♠'),
               ('6',6,'♠'),
               ('7',7,'♠'),
               ('8',8,'♠'),
               ('9',9,'♠'),
               ('10',10,'♠'),
               ('J',10,'♠'),
               ('Q',10,'♠'),
               ('K',10,'♠')]
    cards_diamonds=[('1',1,'d'),
               ('2',2,'♦'),
               ('3',3,'♦'),
               ('4',4,'♦'),
               ('5',5,'♦'),
               ('6',6,'♦'),
               ('7',7,'♦'),
               ('8',8,'♦'),
               ('9',9,'♦'),
               ('10',10,'♦'),
               ('J',10,'♦'),
               ('Q',10,'♦'),
               ('K',10,'♦')]
    
    card_dict={'Diamonds':cards_diamonds,'Hearts':cards_hearts,'Clubs':cards_clubs,'Spades':cards_spades}
    
    randint1=random.randint(0,3)
    randint2=random.randint(0,12)
    
    

    return card_dict[list(card_dict.keys())[randint1]][randint2]


draw_card()


# In[82]:


#This function has been modified

def add_to_hand(hand):
    hand.append(draw_card())
    return hand
player_hand=[]


# In[83]:


def sum_hand(hand):
    val_lst=[index[1] for index in hand]
    return sum(val_lst)


# ♣ ♦ ♥ ♠

# In[84]:


def print_cards(hand,key):
    
    # Notice this function has been modified
    
    if key=="Last":
        card1=["---------------",
                f"|{hand[-1][0]}            |",
                 "|             |",
                 "|             |",
                f"|      {hand[-1][2]}      |",
                 "|             |",
                 "|             |",
                f"|            {hand[-1][0]}|",
                 "---------------"]
        for j in card1:
            print(j, end='\t \n')
    elif key=="All":
        for i in hand:
            
            card1=["---------------",
                f"|{i[0]}            |",
                 "|             |",
                 "|             |",
                f"|      {i[2]}      |",
                 "|             |",
                 "|             |",
                f"|            {i[0]}|",
                 "---------------"]
            for j in card1:
                print(j)

#print(sum_hand(hand))

    #cards=[card1,card2,card3,card4,card5,card6,card7,card8,card9,card10]



# In[85]:


def hit_stand():
    return input('do you want to hit or stand? Enter [S]tand or [H]it').lower().startswith('h')


# In[ ]:





# In[86]:


def check_win(player_hand,dealer_hand):
    
    diff_player=21-(sum_hand(player_hand))
    diff_dealer=21-(sum_hand(dealer_hand))
    
    if diff_player<0:
        print('Dealer wins')
    elif diff_dealer<0:
        print('You win!')  
    elif diff_player>diff_dealer:
        print('You win!')
    elif diff_player<diff_dealer:
        print('Player wins!')
    elif diff_player==diff_dealer:
        print('The game is a draw')
    
    


# In[87]:


deal_test=[('3',3,'♦'),('3',3,'♦'),('2',2,'♦'),('6',6,'♦'),('10',10,'♦')]
play_test=[('5',5,'♣'),('6',6,'♦')]

check_win(play_test,deal_test)


# In[88]:


def replay():
    """Asks player for replay Y/N"""
    return input('Do you want to play again? Enter [Y]es or [N]o ').lower().startswith('y')


# In[ ]:


# Number 2, no inner while loops
from IPython.display import clear_output


turn="Player"
game_on=True


while game_on==True:
    
    clear_output(wait=True)
    print('Welcome to Blackjack!')
    dealer_hand=[] # Initializing lists for hands
    player_hand=[]
    
    print("\n\n")

    print("These are your first two cards")
    add_to_hand(player_hand)
    add_to_hand(player_hand)
    print_cards(player_hand,"All")
    print("Adding up to: ",sum_hand(player_hand),"\n")
    
    print("These are the dealers first two cards")
    add_to_hand(dealer_hand)
    add_to_hand(dealer_hand)
    print_cards(dealer_hand,"All")
    print("Adding up to: ",sum_hand(dealer_hand))
    

    if not hit_stand():
        turn="Dealer"
        print("-------------- YOU STAND --------------")
    else:
        turn="Player"
        print("Player goes")

    if turn=="Player":
        
        while turn=="Player":

            #print("first while loop")
            add_to_hand(player_hand)
            print_cards(player_hand,"Last")
            print("Your current card value is: ",sum_hand(player_hand))
            if sum_hand(player_hand)>21:
                print("You are bust")
                break
            elif sum_hand(player_hand)==21:
                print("GZ, you got 21! Dealers turn")
                turn="Dealer"
            elif hit_stand()==False:
                turn="Dealer"
                print("-------------- YOU STAND --------------")
            
    if turn=="Dealer":
        
        while turn=="Dealer":

            if sum_hand(dealer_hand)>=17:
                if sum_hand(dealer_hand)>21:
                    print("Dealer is bust, You win!")
                    break
                else:
                    print("Dealer cannot draw any more cards")
                    
                    check_win(player_hand,dealer_hand)
                    break
            elif sum_hand(dealer_hand)<=16:
                input("Ready for the next dealer draw? ")
                add_to_hand(dealer_hand)
                print_cards(dealer_hand,"Last")
                print(f"The dealer has drawn a {dealer_hand[-1][0]}, bringing him to a value of {sum_hand(dealer_hand)}")

                
    if replay()==False:
        game_on=False

        
        
        
#if check_win(player_hand , dealer_hand ):


# In[ ]:





# In[ ]:





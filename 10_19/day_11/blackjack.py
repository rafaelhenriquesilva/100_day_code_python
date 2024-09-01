"""
Blackjack

Double-Down or Draw!

Blackjack is an incredibly popular, exciting and easy card game to play. 
The object is to have a hand with a total value higher than the dealer’s without going over 21.
Kings, Queens, Jacks and Tens are worth a value of 10. An Ace has the value of 1 or 11.
The remaining cards are counted at face value.

How To Play
Place a bet in the betting areas marked on the table.
You and fellow players are dealt two cards each whilst the dealer is dealt one face up.
If your first 2 cards add up to 21 (an Ace and a card valued 10), that’s Blackjack!
If they have any other total, decide whether you wish to ‘draw’ or ‘stay’.
You can continue to draw cards until you are happy with your hand.

You may “Double” your original stake on any two-card combination, however, you will only receive one more card.
You can also “Split” any pair (including any two cards with a value of 10) by placing an additional bet equal to your original.
You will then be dealt an additional card to each of your split cards to create two new hands.
If Aces are split, you only receive 1 additional card for each Ace.
If you split Aces and a 10/picture card is drawn, the total is 21, not Blackjack.
If the Dealer has an Ace as their first card, you may stake up to half of your original bet as “Insurance“.
This covers your bet if the dealer gets blackjack. 
If the dealer does get blackjack (drawing 10 as their 2nd card), Insurance wins and will be paid out 2:1.

Once all players have taken their turn the dealer draws another card for their hand.
They must draw until they reach 17 or more.

Rules
Once all cards are drawn, whoever has a total closer to 21 than the dealer wins. 
If player’s hand and dealer’s hand have an equal value, it’s a tie.

All winning bets are paid 1/1 but when you get Blackjack you get paid 3/2.    
"""
import random
dict_cards_game = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Q": 10,
    "J": 10,
    "K": 10,
}

def choice_cards(times):
    list_cards = []
    for _ in range(0, times):
        card_key = random.choice(list(dict_cards_game.keys()))
        list_cards.extend([dict_cards_game[card_key]])
        
    return list_cards

def computer_choices(computer_cards):
    while sum(computer_cards) <= 13:
        computer_cards.extend(choice_cards(1))
        
    return computer_cards

def define_the_winner(personal_cards, computer_cards):
        hand_final_personal = sum(personal_cards)
        hand_final_computer = sum(computer_cards)
        
        print(f"Your final hand: {personal_cards}, sum: {hand_final_personal}")
        print(f"Computer's first card: {computer_cards}, sum: {hand_final_computer}")

        if hand_final_personal <= max_value_game and ((max_value_game - hand_final_personal) < (max_value_game - hand_final_computer)):
            print(f"You win!")
        elif hand_final_computer <= max_value_game and ((max_value_game - hand_final_computer) < (max_value_game - hand_final_personal)):
            print(f"You Lose!")
        elif hand_final_computer == hand_final_personal:
            print('Draw')
        elif hand_final_computer > 21 and hand_final_personal > 21:
            if ((hand_final_computer - max_value_game) < (hand_final_personal - max_value_game)):
                print('You Lose!')
            else:
                print(f"You win!")
        elif hand_final_personal > 21 and hand_final_computer <= 21:
            print('You Lose!')
        

personal_cards = []
start_game = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")
max_value_game = 21
if start_game == 'y':
    personal_cards = choice_cards(2)
    computer_cards = choice_cards(1)
    show_more = True
    while (sum(computer_cards) < 21) and (sum(personal_cards) < 21) and (show_more == True):
        print(f"Your cards: {personal_cards}")
        print(f"Computer's first card: {computer_cards}")
        other_card_decision = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if other_card_decision != 'y':
            computer_cards = computer_choices(computer_cards)
            show_more = False
        else:
            personal_cards.extend(choice_cards(1))
            computer_cards = computer_choices(computer_cards)
            
define_the_winner(personal_cards, computer_cards)
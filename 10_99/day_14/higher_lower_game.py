# Create a Higher Lower Game
import random
import billionaries

TECH_BILLIONAIRES = billionaries.tech_billionaires
INIT_SCORE = 0
INIT_GAME_OVER = False

def choice_billionary(tech_billionaires): 
    tech_billionary_key = random.choice(list(tech_billionaires.keys()))
    return {
        "key":tech_billionary_key,
        "value": tech_billionaires[tech_billionary_key]
            
    }

    

def get_participants_to_competing():
    dict_billions = TECH_BILLIONAIRES
    first_participant = choice_billionary(dict_billions)
    dict_billions.pop(first_participant["key"])
    second_participant = choice_billionary(dict_billions)
    
    return [
        first_participant,
        second_participant
    ]

def make_challenge(competitors):
    dict_answer = {
        "A": competitors[0],
        "B": competitors[1]
    }
    
    print(f'Compare A: {dict_answer['A']['key']}, {dict_answer['A']['value']['description']}.\n')
    print('VS\n')
    print(f'Against B:  {dict_answer['B']['key']}, {dict_answer['B']['value']['description']}.\n')
    
    return dict_answer
    
def compare_participants(dict_answer, answer):
    correct_answer = False
    if(
        answer == 'A' and
        dict_answer[answer]['value']['net_worth'] > dict_answer['B']['value']['net_worth']
    ):
        correct_answer = True
    elif(
        answer == 'B' and
        dict_answer[answer]['value']['net_worth'] > dict_answer['A']['value']['net_worth']
    ):
        correct_answer = True
    
    return correct_answer
    

def higher_lower_game():
    score = INIT_SCORE
    game_over = INIT_GAME_OVER

    while not game_over:
        competitors = get_participants_to_competing()

        dict_answer = make_challenge(competitors)

        richest = ''
        while richest not in ['A', 'B']:
            richest = input("Who has more money? Type 'A' or 'B': ").upper()
            print('\n')
        if compare_participants(dict_answer=dict_answer, answer=richest):
                score += 1
                print(f"You're right! Current score: {score}.\n") 
        else:
                print(f"Sorry, that's wrong. Final score: {score}\n")
                game_over = True
            
higher_lower_game()
    

    

    
    
    
    

import random
import msvcrt
import sys
import time

TITLE_ART = """
rrrrrrr   ppppppp    sssss
r     r   p     p   s     s
r     r   p     p   s
rrrrrrr   ppppppp    ccccc
r  r      p               s
r   r     p         s     s
r   r     p          sssss
"""

moves={'r':'Rock','p':'Paper','s':'Scissors'}
def get_user_choice():
    print("\n choose from (r)ock, (p)aper, (s)cissors",flush=True)
    user_input=""
    while user_input not in ['r','p','s']:
        key_pressed=msvcrt.getch()
        try:
            user_input=key_pressed.decode('utf-8').lower()
        except UnicodeDecodeError:
            continue

        if user_input=='q':
            print("\nQuitting...",flush=True)
            sys.exit()

    print(f"You chose: {moves[user_input]}",flush=True)
    return user_input

def show_loading_bar():
    print("\nComputer Computing...",end="",flush=True)
    for _ in range(20):
        print("█",end="",flush=True)
        time.sleep(0.04)

    print("",flush=True)
    time.sleep(0.3)
    
def get_computer_choice():
    choices=['r','p','s']
    return random.choice(choices)

def get_winner(user,computer):
    if user==computer:
        return "tie"

    if (user=='r' and computer =='s')or\
       (user=='s' and computer =='p')or\
       (user=='p' and computer =='r'):
        return "user"

    return "computer"

def display_result(user_choice,comp_choice,winner):
    
    print(f"\n----Result is-----",flush=True)
    print(f"You chose: {moves[user_choice]}",flush=True)
    print(f"Computer chose:{moves[comp_choice]}",flush=True)
    print("------------------------------------",flush=True)

    if winner=="tie":
        print("It's a Tie!!",flush=True)
    elif winner =="user":
        print("You Win!!",flush=True)
    else:
        print("You Lose",flush=True)

        
def show_startup_bar():
    print("\nLoading......",end="",flush=True)
    for _ in range(30):
        print("█",end="",flush=True)
        time.sleep(0.02)
    print("",flush=True)
    time.sleep(0.5)
print(TITLE_ART,flush=True)
show_startup_bar()

print("Welome to Rock, Paper, Scissors! (Press 'q'to quit)",flush=True)

print("Welome (Press 'q' to quit at any time)", flush=True)



while True:
    user_choice = get_user_choice()
    show_loading_bar()
    comp_choice = get_computer_choice()

    winner = get_winner(user_choice,comp_choice)
    display_result(user_choice,comp_choice,winner)
    print("\nHow about a rematch cause this goes for Eternity! (y/n): ",flush=True)
    play_again = ""
    while play_again not in ['y','n']:
        key_pressed = msvcrt.getch()
        try:
            play_again=key_pressed.decode('utf-8').lower()
        except UnicodeDecodeError:
            continue
    print(f"You pressed :{play_again}",flush=True)
    
    if play_again =='n' or play_again =='q':
        print("\n",flush=True)
        break
print("Until Next time",flush=True)

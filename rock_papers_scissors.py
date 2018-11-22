import random
import math


def init_game():
    print("Welcome to Rock, Paper, Scissor Game!!!")
    try:
        playing_times = int(input("Enter number of times you want to play the game? Maximum wins among the lot wins the league! "))
        print()
        play_game(playing_times)
    except KeyboardInterrupt:
        print("Keyboard Interrupt! Exiting!")
        return
    except Exception as e:
        print("Wrong input! Please correct and try again")
        return


def play_game(playing_times):
    user_wins = 0
    computer_wins = 0
    win_number = math.ceil(playing_times / 2) if playing_times % 2 != 0 else playing_times / 2 + 1

    while playing_times:
        user_choice = input("Enter rock(r), paper(p) or scissors(s)? ")
        valid_choices = ["r", "p", "s"]
        if user_choice in valid_choices:
            computer_choice = random.choice(valid_choices)
            user_win_status = evaluate_output(computer_choice, user_choice)
            print({0: "DRAW!!!!", 1: "YOU WON!!!!", -1: "YOU LOST!!!!"}[user_win_status])
            if user_win_status == 1:
                user_wins = user_wins + 1
            if user_win_status == -1:
                computer_wins = computer_wins + 1
            if win_number == user_wins:
                print()
                print("YOU WON THE LEAGUE!!!! Yaay!!")
                return
            if win_number == computer_wins:
                print()
                print("YOU LOST THE LEAGUE!!!! Hard luck!!")
                return
            print()
        else:
            print("You have entered something stupid!! Please retry the game!")
            return
        playing_times -= 1
    print()
    print("THE LEAGUE IS A DRAW!!!")


def evaluate_output(cc, uc):
    print("Computer chose {} and You chose {}".format(prettify(cc), prettify(uc)))
    if cc == uc:
        return 0
    if cc == "r":
        if uc == "p":
            return 1
        return -1
    if cc == "p":
        if uc == "s":
            return 1
        return -1
    if cc == "s":
        if uc == "r":
            return 1
        return -1

def prettify(input):
    return {
        'r': "Rock(O)",
        'p': "Paper(__)",
        's': "Scissor(8<)"
    }[input]


init_game()
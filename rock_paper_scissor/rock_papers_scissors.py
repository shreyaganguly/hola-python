import random
import math



def init_rock_paper_scissor_game():
    print("Welcome to Rock, Paper, Scissor Game!!!")
    try:
        playing_times = int(input("Enter number of times you want to play the game? Maximum wins among the lot wins the league! "))
        print()
        play_game(playing_times)
    except KeyboardInterrupt:
        print("Keyboard Interrupt! Exiting!")
        return
    except Exception:
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
            print(get_game_status(user_win_status))
            user_wins, computer_wins = evaluate_per_outcome_result(user_win_status, user_wins, computer_wins)
            if evaluate_league_outcome(0, win_number, user_wins, computer_wins) == 1:
                return
        else:
            print("Wrong input! Please correct and try again")
            return
        playing_times -= 1
    evaluate_league_outcome(1, 0, user_wins, computer_wins)


def evaluate_league_outcome(end_of_match, win_number, user_wins, computer_wins):
    if end_of_match == 1:
        if user_wins > computer_wins:
            print_outcome(1)
            return 1
        if user_wins < computer_wins:
            print_outcome(-1)
            return 1
        print_outcome(0)
        return 1
    if win_number == user_wins:
        print_outcome(1)
        return 1
    if win_number == computer_wins:
        print_outcome(-1)
        return 1
    print()


def evaluate_per_outcome_result(user_win_status, user_wins, computer_wins):
    if user_win_status == 1:
        return user_wins + 1, computer_wins
    if user_win_status == -1:
        return user_wins, computer_wins + 1

    return user_wins, computer_wins


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


def get_game_status(user_win_status):
    return {
        0: "DRAW!!!!",
        1: "YOU WON!!!!",
        -1: "YOU LOST!!!!"
    }[user_win_status]


def print_outcome(user_win_status):
    outcome = {
        0: "THE LEAGUE IS A DRAW!!!",
        -1: "YOU LOST THE LEAGUE!!!! Hard luck!!",
        1: "YOU WON THE LEAGUE!!!! Yaay!!"
    }[user_win_status]
    print()
    print(outcome)

init_rock_paper_scissor_game()

from game_logic import GameLogic

playing = True


def welcome():
    print("Welcome to Ten Thousand")
    choice = input("(y)es to play or (n)o to decline: \n> ")
    if choice == "n":
        print("OK. Maybe another time")
        global playing
        playing = False
    else:
        print("Starting Round 1")


def play(roller=GameLogic.roll_dice):
    round_num = 1
    total_score = 0
    all_kept_dice = []
    kept_score = []
    round_score = 0
    while playing:
        print(f"Rolling {6 - len(all_kept_dice)} dice...")

        roll_string = ""
        roll_list = []

        roll = roller(6 - len(all_kept_dice))
        for x in roll:
            roll_string += str(x) + " "
            roll_list.append(x)
        print(f"*** {roll_string} ***")
        if GameLogic.calculate_score(tuple(roll_list)) == 0:
            print("You zilched!")
            round_num += 1
            print(f"Your total score is {total_score} points.")
            print(f"Starting Round {round_num}")
        else:
            print("Enter dice to keep, or (q)uit:")
            keepers = input("> ")
            if keepers == "q":
                print(f"Thanks for playing. You earned {total_score} points.")
                break
            for x in keepers:
                all_kept_dice.append(int(x))
                kept_score.append(int(x))
            round_score += GameLogic.calculate_score(tuple(kept_score))
            print(f"You have {round_score} unbanked points and {6 - len(all_kept_dice)} dice remaining.")
            print("(r)oll again, (b)ank your points or (q)uit:")
            choice = input("> ")
            if choice == "q":
                print(f"Thanks for playing. You earned {total_score} points.")
                break
            elif choice == "b":
                total_score += round_score
                print(f"You banked {round_score} in round {round_num}")
                round_num += 1
                print(f"Total score is {total_score} points")
                all_kept_dice = []
                round_score = 0
                print(f"Starting Round {round_num}")
            kept_score = []




if __name__ == '__main__':
    welcome()
    play()
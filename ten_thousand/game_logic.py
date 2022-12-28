from random import randint
from collections import Counter


class GameLogic:
  #build GameLogic class
    @staticmethod
   #build roll dice function that rolls dice and stores them in tuple

    def roll_dice(num_dice):
        values = []
        for i in range(num_dice):
            value = randint(1, 6)
            values.append(value)
        return tuple(values)

    @staticmethod
    # Calculates Scores and references them to test value to determine output
    def calculate_score(values):
        score = 0
        counts = Counter(values)
        pair_counter = 0

        for die in counts:
            if counts[die] == 2:
                pair_counter += 1
            if pair_counter < 3 and len(counts) < 6:
                if die == 1:
                    if counts[die] == 1:
                        score += 100
                    elif counts[die] == 2:
                        score += 200
                    elif counts[die] == 3:
                        score += 1000
                    elif counts[die] == 4:
                        score += 2000
                    elif counts[die] == 5:
                        score += 3000
                    elif counts[die] == 6:
                        score += 4000
                if die == 2:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 200
                    elif counts[die] == 4:
                        score += 400
                    elif counts[die] == 5:
                        score += 600
                    elif counts[die] == 6:
                        score += 800
                if die == 3:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 300
                    elif counts[die] == 4:
                        score += 600
                    elif counts[die] == 5:
                        score += 900
                    elif counts[die] == 6:
                        score += 1200
                if die == 4:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 400
                    elif counts[die] == 4:
                        score += 800
                    elif counts[die] == 5:
                        score += 1200
                    elif counts[die] == 6:
                        score += 1600
                if die == 5:
                    if counts[die] == 1:
                        score += 50
                    elif counts[die] == 2:
                        score += 100
                    elif counts[die] == 3:
                        score += 500
                    elif counts[die] == 4:
                        score += 1000
                    elif counts[die] == 5:
                        score += 1500
                    elif counts[die] == 6:
                        score += 2000
                if die == 6:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 600
                    elif counts[die] == 4:
                        score += 1200
                    elif counts[die] == 5:
                        score += 1800
                    elif counts[die] == 6:
                        score += 2400
        if pair_counter == 1 and counts[die] == 3:
            score = 1500
        if pair_counter == 3:
            score = 1500
        if len(counts) == 6:
            score = 1500
        return score


        # find count of each number rolled

        # if count is 3: score is number times 100
            # else if it's three 1s: 1000 points
            # else if there are 3 of a kind and a pair: 1500 points

        # if count is 4: score is number times 100 times 2
            # else if it's four 1s: 2000 points

        # if count is 5: score is number times 100 times 4
            # else if it's five 1s: 4000 points

        # if count is 6: score is number times 100 times 8
            # else if it's six 1s: 8000 points

        # if count < 3: determine if number is a 1 or 5
            # if 1: each 1 is worth 100 points
            # if 5: each 5 is worth 50 points
            # else if there are three pairs: 1500 points
            # else if there's a straight 1-6: 2000 points
            # else: 0 points
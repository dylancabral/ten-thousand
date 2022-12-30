from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def validate_keepers(dice_roll, dice_kept):
        dice_roll_validation = Counter(dice_roll)
        dice_kept_validation = Counter(dice_kept)

        if len(dice_kept_validation) <= len(dice_roll_validation):
            if all(dice_kept_validation[key] <= dice_roll_validation[key] for key in dice_kept_validation.keys()):
                return True
            return False
        else:
            return False

    @staticmethod
    def roll_dice(number):
        return tuple(randint(1, 6) for x in range(0, number))

    @staticmethod
    # Calculates Scores and references them to test value to determine output
    def calculate_score(dice_roll):
        dice_count = Counter(dice_roll)

        score_dict = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

        score = 0

        # calculate straight
        if len(dice_count) == 6:
            return 1500

        # calculate triple doubles
        if len(dice_count) == 3 and all(value == 2 for value in dice_count.values()):
            return 1500

        # score based on face value
        for face_value, count in dice_count.items():
            if face_value == 5 and count <= 2:
                score += 50 * count
            elif face_value == 1 and count <= 2:
                score += 100 * count
            elif face_value == 1 and count == 3:
                score += 1000
            elif count == 3:
                score += score_dict[face_value]
            elif count == 4:
                score += score_dict[face_value] * 2
            elif count == 5:
                score += score_dict[face_value] * 3
            elif count == 6:
                score += score_dict[face_value] * 4

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
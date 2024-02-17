def undoom_dice(original_sums):
    """Finds transformed dice with matching probabilities."""

    diceA = find_dice_combinations(1, 5)
    diceB = find_dice_combinations(1, 12)

    for dice1 in diceA:
        for dice2 in diceB:
            temp_sums = calculate_sum_probabilities(dice1, dice2)
            if temp_sums == original_sums:
                return dice1, dice2, temp_sums

def find_dice_combinations(start_value, limit):
    """Generates all possible 6-sided dice combinations."""

    combinations = []
    def helper(current, temp):
        if len(temp) == 6:
            combinations.append(temp)
            return
        for i in range(current, limit + 1):
            helper(i, temp + [i])
    helper(start_value, [])
    return combinations

def calculate_sum_probabilities(dice1, dice2):
    """Calculates probabilities for sums of two dice."""

    temp_sums = {}
    for value1 in dice1:
        for value2 in dice2:
            sum_value = value1 + value2
            temp_sums[sum_value] = temp_sums.get(sum_value, 0) + 1
    return temp_sums

# Example usage:
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]
original_sums = calculate_sum_probabilities(Die_A, Die_B)

new_dice_A, new_dice_B, new_sums = undoom_dice(original_sums)
print(f"New Dice A: {new_dice_A}")
print(f"New Dice B: {new_dice_B}")

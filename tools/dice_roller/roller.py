import random


def roll_dice(sides:int, count:int):
    result = []
    for i in range(count):
        die_roll = random.randint(1,sides)
        result.append(die_roll)
    return result
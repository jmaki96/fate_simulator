""" Define the different functions for rolling Fate dice.
"""
from enum import Enum
import random
from typing import List


class RerollType(Enum):
    """ A RerollType is how rerolls are handled when determining the result of a die roll.
    """

    TakeBest = 0  # Take the best outcome across all rerolls
    TakeWorst = 1  # Take the worst outcome across all rerolls
    TakeLast = 2  # Take the most recent outcome across all rerolls


def _roll_fudge_die(num_dice: int = 4, modifier: int = 0) -> int:
    """ Rolls fudge dice, which have a uniform chance to be a result of -1, 0, or 1. Sums and returns the value.

    Args:
        num_dice (int, optional): Number of fudge dice to roll and sum. Defaults to 4.
        modifier (int, optional): Flat integer to add to result. Defaults to 0.

    Returns:
        int: Total result of all fudge dice
    """

    total = modifier

    for die in range(num_dice):
        roll = random.randrange(-1,2,1)  # range is inclusive of start, exclusive of stop

        total += roll

    return total


def roll_fudge_dice(num_dice: int = 4, 
                    modifier: int = 0, 
                    num_rerolls: int = 0,
                    reroll_type: RerollType = RerollType.TakeLast) -> int:
    """ Rolls and rerolls fudge dice, which have a uniform chance to be a result of -1, 0, or 1. Sums and returns the value.


    Args:
        num_dice (int, optional): Number of fudge dice to roll and sum. Defaults to 4.
        modifier (int, optional): Flat integer to add to result. Defaults to 0.
        num_rerolls (int, optional): How many times to reroll the dice. Defaults to 0.
        reroll_type (RerollType, optional): How to handle rerolls. Defaults to taking the last outcome

    Returns:
        int: Total result of all fudge dice across rerolls by RerollType
    """

    totals: List[int] = []

    for roll in range(num_rerolls + 1):  # plus 1, because you always roll at least once
        totals.append(_roll_fudge_die(num_dice, modifier))

    if reroll_type == RerollType.TakeLast:
        return totals[-1]
    elif reroll_type == RerollType.TakeBest:
        return max(totals)
    elif reroll_type == RerollType.TakeWorst:
        return min(totals)
    else:
        raise ValueError(f"Unknown RerollType of {reroll_type}")

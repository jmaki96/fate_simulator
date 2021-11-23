import logging
import time
import argparse

import __init__  # register core library

from core.roll import roll_fudge_dice, RerollType

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    start_time = time.time()

    # Load arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-n', '--num_dice', default=4, type=int)
    parser.add_argument('-m', '--modifier', default=0, type=int)
    parser.add_argument('-r', '--num_rerolls', default=0, type=int)
    parser.add_argument('-t', '--reroll_type', default='last')
    args = parser.parse_args()

    reroll_type: str = args.reroll_type.lower()
    reroll_type_enum: RerollType = None

    if reroll_type == "last":
        reroll_type_enum = RerollType.TakeLast
    elif reroll_type == "best":
        reroll_type_enum = RerollType.TakeBest
    elif reroll_type == "worst":
        reroll_type_enum = RerollType.TakeWorst
    else:
        raise argparse.ArgumentError(f"Unknown RerollType of {reroll_type}")
    
    if args.modifier > 0:
        sign = '+'
    else:
        sign = ''

    _logger.info(f"Rolling: {args.num_dice}dF{sign}{args.modifier} {args.num_rerolls} times taking the {reroll_type} result.")
    result = roll_fudge_dice(args.num_dice, args.modifier, args.num_rerolls, reroll_type_enum)
    _logger.info(f"Result: {result}")
    

    end_time = time.time()
    _logger.info("Script finished in {0:.2f}s".format(end_time-start_time))
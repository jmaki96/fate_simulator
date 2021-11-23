import logging
from os import write
import time
import argparse
from statistics import mean
from typing import Dict, List

import __init__  # register core library

from core.roll import roll_fudge_dice, RerollType
from core.utilities.reports import write_report, generate_report_path

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    start_time = time.time()

    # Load arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--sample_size', default=10000, type=int, help='How many trials to average across')
    args = parser.parse_args()

    # === Average improvement based on initial roll value === 
    data: List[Dict[str, str]] = []  # List of List of fields
    headers: List[str] = ["Initial Value", "TakeLast", "TakeBest", "TakeWorst"]  # List of Headers
    
    for initial_value in range(-4, 5, 1):  # range is inclusive of the start, exclusive of the stop
        datum: Dict[str, str] = {"Initial Value": str(initial_value)}
        for reroll_type in (RerollType.TakeLast, RerollType.TakeBest, RerollType.TakeWorst):
            improvements: List[int] = []
            for trial in range(args.sample_size):
                new_value = roll_fudge_dice()

                if reroll_type == RerollType.TakeLast:
                    improvement = new_value - initial_value
                elif reroll_type == RerollType.TakeBest:
                    improvement = max(new_value, initial_value) - initial_value
                elif reroll_type == RerollType.TakeWorst:
                    improvement = min(new_value, initial_value) - initial_value
                
                # _logger.debug(f"{reroll_type.name} - init: {initial_value} new: {new_value} improv: {improvement}")
                improvements.append(improvement)
                
            datum[reroll_type.name] = str(mean(improvements))

        data.append(datum)

    report_path = generate_report_path("model_roll_outcomes")
    write_report(report_path, headers, data)

    end_time = time.time()
    _logger.info("Script finished in {0:.2f}s".format(end_time-start_time))
""" Utilities for writing simple CSV style reports
"""

from typing import List
import os

from core.settings import REPORT_DIRECTORY, DATESTAMP


def generate_report_path(report_name: str, report_extension: str = "csv") -> str:
    """ Creates a fully qualified path to report directory with timestamped name and specified extension
    Args:
        report_name (str): The name to timestamp
        report_extension (str, optional): File extension for the report. Exclude the period. Defaults to "csv".
    Returns:
        str: Fully qualified path to the report directory with the name and extension like REPORT_DIRECTORY/report_name_DATESTAMP.extension
    """

    return os.path.join(REPORT_DIRECTORY, f"{report_name}_{DATESTAMP}.{report_extension}")


def write_report(report_path: str, report_headers: List[str], report_contents: List[dict], delimiter: str = ',') -> None:
    """ Takes a path, headers, and a list of Dicts and writes that to a .csv
    Args:
        report_path (str): The path to write the report to (All folders must exist)
        report_headers (List[str]): The headers, in order, to write
        report_contents (List[dict]): The list of rows (as dicts) to write
        delimiter (str): Delimiter to use between fields, defaults to ,
    """

    with open(report_path, "w+") as report_h:
        report_h.write(delimiter.join(report_headers) + "\n")

        for row in report_contents:
            line_fields = []
            for field in report_headers:
                field_formatted = str(row.get(field)).replace('"', "")  # remove "" escape characters

                if "," in field_formatted:
                    field_formatted = f'"{field_formatted}"'  # Escape commas with ""

                line_fields.append(field_formatted)
            report_h.write(delimiter.join(line_fields) + "\n")

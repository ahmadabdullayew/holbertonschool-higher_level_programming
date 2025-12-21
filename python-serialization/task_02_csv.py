#!/usr/bin/env python3
"""
Convert CSV file into a JSON file (data.json)
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads CSV data and writes JSON to data.json.
    Returns True if successful, False otherwise.
    """
    try:
        data_list = []

        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(dict(row))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False

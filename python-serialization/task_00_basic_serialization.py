#!/usr/bin/env python3
"""
Basic serialization module:
 - Serialize a Python dictionary to a JSON file.
 - Deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary to JSON and saves it to a file.
    Overwrites file if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON content from a file.
    Returns a dictionary recreated from JSON.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

#!/usr/bin/env python3
"""
Serialization and deserialization using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception:
        return False

    return True


def deserialize_from_xml(filename):
    """
    Deserializes XML content from a file and returns a Python dict.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            # All XML text comes in as strings
            result[child.tag] = child.text

        return result

    except Exception:
        return None

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary.get(key, value)
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))

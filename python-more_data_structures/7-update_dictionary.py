#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
